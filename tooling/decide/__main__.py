"""CLI entrypoint: python3 -m tooling.decide context <target-repo> [--out PATH]
                    python3 -m tooling.decide apply <target-repo> <decisions.yaml> [--out PATH]

Suite document paths default to this repo's own docs/*.md next to tooling/decide/
(the normal case: this tool runs from within the design-suite repo against a
downstream target-repo path) but can be overridden with --composition/--constraints/
--decision for testing or for a vendored copy of this suite elsewhere.
"""
import argparse
import os
import sys

import yaml

from .apply_cmd import run_apply
from .context_cmd import run_context

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_COMPOSITION = os.path.join(REPO_ROOT, "docs", "composition-1.0.0.md")
DEFAULT_CONSTRAINTS = os.path.join(REPO_ROOT, "docs", "constraints-1.0.0.md")
DEFAULT_DECISION = os.path.join(REPO_ROOT, "docs", "decision-1.0.0.md")


def _add_suite_path_args(p):
    p.add_argument("--composition", default=DEFAULT_COMPOSITION)
    p.add_argument("--constraints", default=DEFAULT_CONSTRAINTS)
    p.add_argument("--decision", default=DEFAULT_DECISION)
    p.add_argument("--out", default=None, help="write output here instead of stdout")


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python3 -m tooling.decide")
    sub = parser.add_subparsers(dest="command", required=True)

    context_p = sub.add_parser("context", help="emit the decision context for a target repo")
    context_p.add_argument("target_repo")
    _add_suite_path_args(context_p)

    apply_p = sub.add_parser("apply", help="validate and write decisions for a target repo")
    apply_p.add_argument("target_repo")
    apply_p.add_argument("decisions_path")
    _add_suite_path_args(apply_p)

    args = parser.parse_args(argv)

    if args.command == "context":
        result = run_context(args.target_repo, args.composition, args.constraints, args.decision)
        exit_code = 0
    else:
        result = run_apply(
            args.target_repo, args.decisions_path, args.composition, args.constraints, args.decision
        )
        exit_code = 1 if result["rejected"] else 0

    output = yaml.safe_dump(result, sort_keys=False, default_flow_style=False, width=100)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(output)
    else:
        print(output)

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
