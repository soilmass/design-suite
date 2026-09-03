#!/usr/bin/env python3
"""Decision-completeness checker. Joins a project's ADR set against the Composition
family registry and reports which of the 67 families are decided and which are
still running on defaults. This is the build `audit/tooling-audit-2.0.0.md` Part VI
item 2 recommends -- see README.md and ROADMAP.md Phase 2.

This suite's own repo has no ADRs (Composition's families are choices a *team
building a website* makes, not choices this repo makes) -- so this tool is meant
to be run by downstream consumers against their own project's ADR directory.

ADR format this tool expects, one file per decision:

    ```yaml
    id: ADR-0001
    title: Primary conversion goal is trial signup
    status: accepted          # optional, defaults to accepted
    date: 2026-08-14          # optional
    families:                 # required -- F## or F##.# ids this ADR decides
      - F01
      - F01.2
    deciders: [maya, chen]    # optional
    ```

    # ADR-0001 - Primary conversion goal is trial signup

    ## Context
    ...

    ## Decision
    ...

    ## Consequences
    ...

The front matter block must be the first thing in the file -- a fenced ```yaml
block, same convention this suite's own documents use. `families:` is the only
required field; it is a list of Composition ids the ADR addresses (segment ids
like F01.2 roll up to their parent family for the completeness report). Only
ADRs with `status: accepted` (the default when the field is omitted) count as
addressing a family -- `proposed`, `rejected`, and `superseded` do not, so a
family with only a proposed ADR still reports as not yet decided.

One ADR per file, any filenames, anywhere under the directory you point this at
(scanned recursively). See tests/decision_completeness/fixtures/ for worked
examples, including the empty-directory case.

Usage:
    python3 decision_completeness.py <adr-dir> [--registry PATH]
"""
import re, sys, os, glob, yaml

DEFAULT_REGISTRY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'registry.yaml')

FAMILY_LIKE = re.compile(r'^(F\d{2})(?:\.\d+)?$')


def front_matter(t):
    m = re.match(r'```yaml\n(.*?)\n```', t, re.S)
    return yaml.safe_load(re.sub(r'\s+#.*', '', m.group(1))) if m else None


def load_families(registry_path):
    reg = yaml.safe_load(open(registry_path)) or []
    all_ids = {r['id'] for r in reg}
    families = {r['id']: r['name'] for r in reg if r.get('owner') == 'composition' and r.get('type') == 'family'}
    return families, all_ids


def load_adrs(adr_dir):
    files = sorted(glob.glob(os.path.join(adr_dir, '**', '*.md'), recursive=True))
    adrs, malformed = [], []
    for path in files:
        text = open(path, encoding='utf-8').read()
        rel = os.path.relpath(path, adr_dir)
        fm = front_matter(text)
        if not fm:
            malformed.append((rel, 'no leading ```yaml front matter block'))
            continue
        fams = fm.get('families')
        if not fams:
            malformed.append((rel, 'front matter has no families: list'))
            continue
        status = str(fm.get('status', 'accepted')).strip().lower()
        adrs.append(dict(path=rel, families=fams, status=status))
    return adrs, malformed


def main(argv):
    if not argv or argv[0] in ('-h', '--help'):
        print(__doc__)
        return 0 if argv else 2

    adr_dir = argv[0]
    registry_path = DEFAULT_REGISTRY
    if '--registry' in argv:
        registry_path = argv[argv.index('--registry') + 1]

    print("=" * 64)
    print("DECISION COMPLETENESS")
    print("=" * 64)

    if not os.path.isfile(registry_path):
        print(f"\nERROR: registry not found at {registry_path}")
        print("Run tooling/validate.py in the design-suite repo first, or pass --registry.")
        return 1
    if not os.path.isdir(adr_dir):
        print(f"\nERROR: {adr_dir} is not a directory")
        return 1

    families, all_ids = load_families(registry_path)
    adrs, malformed = load_adrs(adr_dir)

    print(f"\n[1] Registry")
    print(f"  {registry_path} -> {len(families)} Composition families")

    print(f"\n[2] ADR scan")
    print(f"  {adr_dir} -> {len(adrs)} ADR(s) read, {len(malformed)} malformed")
    for rel, why in malformed:
        print(f"    SKIPPED  {rel}: {why}")

    problems = [f"malformed ADR {rel}: {why}" for rel, why in malformed]

    # join: family -> list of (adr path, status, cited id)
    joined = {fid: [] for fid in families}
    for adr in adrs:
        for cited in adr['families']:
            cited = str(cited).strip().upper()
            m = FAMILY_LIKE.match(cited)
            if not m:
                problems.append(f"{adr['path']}: '{cited}' is not a Composition family/segment id")
                continue
            if cited not in all_ids:
                problems.append(f"{adr['path']}: unknown id '{cited}' cited")
                continue
            parent = m.group(1)
            if parent not in families:
                problems.append(f"{adr['path']}: '{cited}' does not resolve to a Composition family")
                continue
            joined[parent].append((adr['path'], adr['status'], cited))

    print(f"\n[3] Family completeness")
    ok = pending = unaddressed = 0
    for fid in sorted(families, key=lambda x: (len(x), x)):
        entries = joined[fid]
        accepted = [e for e in entries if e[1] == 'accepted']
        if accepted:
            ok += 1
            marker = 'ok'
            by = ', '.join(sorted({f"{p} ({c})" for p, s, c in accepted}))
        elif entries:
            pending += 1
            marker = 'pending'
            by = ', '.join(sorted({f"{p} [{s}]" for p, s, c in entries}))
        else:
            unaddressed += 1
            marker = 'unaddressed'
            by = '-'
        print(f"  {fid:5} {families[fid]:28} {marker:12} {by}")

    total = len(families)
    print("\n" + "=" * 64)
    print(f"{ok}/{total} addressed, {pending} pending, {unaddressed} unaddressed")
    if problems:
        print(f"{len(problems)} PROBLEM(S)")
        for p in problems:
            print("  -", p)
    else:
        print("PASS -- no malformed ADRs, no unresolved citations")
    print("=" * 64)
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
