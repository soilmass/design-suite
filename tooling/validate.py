#!/usr/bin/env python3
"""Suite validator. Extracts IDs, builds the registry, checks the dependency rule."""
import re, sys, os, yaml, json

TIER = {'vocabulary':0,'constraints':0,'anatomy':1,'composition':1,
        'decision':2,'implementation':2,'verification':3,'diagnosis':3,'governance':None}
NS   = {'V':'vocabulary','A':'anatomy','F':'composition','C':'constraints',
        'D':'decision','T':'implementation','K':'implementation','X':'verification',
        'R':'diagnosis','G':'governance'}

DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs')

DOCS = {'vocabulary':'vocabulary-1.0.0.md',
        'anatomy':'anatomy-1.0.0.md',
        'composition':'composition-1.0.0.md',
        'constraints':'constraints-1.0.0.md',
        'decision':'decision-1.0.0.md',
        'implementation':'implementation-1.0.0.md',
        'verification':'verification-1.0.0.md',
        'diagnosis':'diagnosis-1.0.0.md',
        'governance':'governance-1.0.0.md'}

def front_matter(t):
    m = re.match(r'```yaml\n(.*?)\n```', t, re.S)
    return yaml.safe_load(re.sub(r'\s+#.*','',m.group(1))) if m else None

def defined(name, t):
    if name=='composition':
        fam = re.findall(r'^### (F\d\d) · (.+)$', t, re.M)
        seg = re.findall(r'\*\*(F\d\d\.\d)\*\* ([^—\n]+)', t)
        return [(i,n.strip(),'family') for i,n in fam] + [(i,n.strip(),'segment') for i,n in seg]
    if name=='constraints':
        return [(i,n.strip(),'constraint') for i,n in re.findall(r'^\*\*(C\d{3}) · (.+?)\*\*', t, re.M)]
    if name=='vocabulary':
        return [(i,n.strip(),'term') for i,n in re.findall(r'\*\*(V-\d{3}) · (.+?)\*\*', t)]
    if name=='anatomy':
        return [(i,n.strip(),'anatomy entry') for i,n in re.findall(r'^#{2,3} (A-\d{3}) · (.+)$', t, re.M)]
    if name=='governance':
        return [(i,n.strip(),'process rule') for i,n in re.findall(r'^## (G\d{3}) · (.+)$', t, re.M)]
    if name=='diagnosis':
        return [(i,n.strip(),'read rule') for i,n in re.findall(r'^## (R\d{3}) · (.+)$', t, re.M)]
    if name=='verification':
        return [(i,n.strip(),'check') for i,n in
                re.findall(r'^## (X\d{3}) · (.+)$', t, re.M) + re.findall(r'^\| (X\d{3}) ([A-Z][^|]+)\|', t, re.M)]
    if name=='implementation':
        return [(i,n.strip(),'token' if i[0]=='T' else 'build rule')
                for i,n in re.findall(r'^\*\*([TK]\d{3}) · (.+?)\*\*', t, re.M)
                          + re.findall(r'^## ([TK]\d{3}) · (.+)$', t, re.M)]
    if name=='decision':
        return [(i,n.strip(),'rule') for i,n in re.findall(r'^## (D\d{3}) · (.+)$', t, re.M)]
    return []

docs, allids, problems = {}, {}, []
for name, path in DOCS.items():
    t = open(os.path.join(DOCS_DIR, path)).read()
    fm = front_matter(t)
    ids = defined(name, t)
    docs[name] = dict(text=t, fm=fm, ids=ids)
    for i,n,k in ids:
        if i in allids: problems.append(f"DUPLICATE ID {i} in {name} and {allids[i][0]}")
        allids[i] = (name, n, k)

print("="*64); print("SUITE VALIDATION"); print("="*64)

# 1 front matter + declared exports
print("\n[1] Front matter and declared exports")
for name, d in docs.items():
    fm = d['fm']
    if not fm: problems.append(f"{name}: no front matter"); continue
    declared_tier = fm.get('tier')
    if TIER[name] is None:
        if not str(declared_tier).startswith('none'):
            problems.append(f"{name}: expected tier 'none', got {declared_tier}")
    elif declared_tier != TIER[name]:
        problems.append(f"{name}: tier {declared_tier} != {TIER[name]}")
    top = [i for i,_,k in d['ids'] if k in ('family','constraint','rule','term','token','build rule','anatomy entry','check','read rule','process rule')]
    byns = {}
    for i in top: byns.setdefault(i[0], []).append(i)
    actual = ', '.join(f"{min(v)}–{max(v)}" for k,v in sorted(byns.items()))
    dec = str(fm.get('exports',''))
    decl = {m[0]: m for m in [re.findall(r'([A-Z]-?\d+)', p) for p in dec.split(',')] if m}
    ok = True
    for ns, v in sorted(byns.items()):
        d_ns = next((m for m in decl.values() if m[0][0]==ns), None)
        if not d_ns or d_ns[0]!=min(v) or d_ns[-1]!=max(v): ok = False
    print(f"  {name:14} v{fm['version']:8} tier {fm['tier']}  declared {dec:30} actual {actual:24} {'ok' if ok else 'MISMATCH'}")
    if not ok: problems.append(f"{name}: declares {dec}, actual {actual}")

# 2 dependency direction
print("\n[2] Dependency direction (downward only)")
for name, d in docs.items():
    for dep in (d['fm'].get('depends') or []):
        dn = dep.split()[0].lower()
        dt, mt = TIER.get(dn), TIER[name]
        exists = dn in DOCS
        verdict = 'ok' if (dt is not None and dt < mt) else 'ILLEGAL'
        if verdict=='ILLEGAL': problems.append(f"{name} -> {dn}: not downward")
        print(f"  {name:13} -> {dn:13} tier {dt} < {mt}  {verdict}{'' if exists else '   [TARGET NOT BUILT]'}")

# 3 cross-references
print("\n[3] Cross-reference resolution")
for name, d in docs.items():
    cited = set(re.findall(r'\b(V-\d{3}|[FCDAXRG]\d{2,3}(?:\.\d)?)\b', d['text']))
    cited = {c for c in cited if c[0] in NS and NS[c[0]] != name}
    unres = sorted(c for c in cited if c not in allids)
    ext   = sorted(c for c in unres if NS[c[0]] not in DOCS)
    dang  = sorted(c for c in unres if NS[c[0]] in DOCS)
    print(f"  {name:13} cites {len(cited):3} external   dangling: {dang or 'none'}")
    for c in dang: problems.append(f"{name}: dangling {c}")

# 4 registry
reg = [dict(id=i, owner=o, name=n, type=k, status='active', since='1.0.0')
       for i,(o,n,k) in sorted(allids.items())]
yaml.safe_dump(reg, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'registry.yaml'),'w'), sort_keys=False, allow_unicode=True, width=200)
print(f"\n[4] Registry written: {len(reg)} entries -> registry.yaml")
from collections import Counter
for k,v in sorted(Counter(x['type'] for x in reg).items()): print(f"  {k:12} {v}")

print("\n[4b] Orthogonality — documents declaring cites_no_ids must cite none")
for name, d in docs.items():
    if d['fm'].get('cites_no_ids'):
        foreign = sorted({c for c in re.findall(r'\b(V-\d{3}|[FCDAXR]\d{2,3}(?:\.\d)?)\b', d['text'])})
        print(f"  {name:15} declares cites_no_ids  found: {foreign or 'none'}  {'ok' if not foreign else 'VIOLATION'}")
        if foreign: problems.append(f"{name}: declares cites_no_ids but cites {foreign}")

print("\n[5] Roster")
for n_,t_ in sorted(TIER.items(), key=lambda x:(x[1] is None, x[1] or 0, x[0])):
    print(f"  {n_:15} tier {str(t_):4} {'BUILT' if n_ in DOCS else 'not built'}")
missing=[n_ for n_ in TIER if n_ not in DOCS]
print(f"  -> {len(DOCS)} built, {len(missing)} remaining: {', '.join(sorted(missing))}")

print("\n" + "="*64)
if problems:
    print(f"{len(problems)} PROBLEM(S)"); [print("  -",p) for p in problems]
else:
    print("PASS — no problems")
print("="*64)
