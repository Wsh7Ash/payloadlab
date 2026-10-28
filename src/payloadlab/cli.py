"""payloadlab command line interface.

Shared subcommands (validate / list / show / search / build) exist in every
skill pack built on this harness; ``poc`` is payloadlab's domain command: it
turns a structured test brief into a phase-grouped proof-of-concept
authoring runbook drawn from the corpus.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from . import __version__
from .corpus import PACK, SKILLS
from .render import build_pack, render_skill, word_count
from .validate import (
    MAX_DESCRIPTION,
    MIN_DONE,
    MIN_PATTERNS,
    MIN_PITFALLS,
    MIN_SIGNALS,
    MIN_STEPS,
    MIN_SUMMARY,
    MIN_WORDS,
    Issue,
    validate_pack,
)

PHASE_ORDER = ("scope", "hypothesis", "craft", "deliver", "observe", "report")

FLOORS = {
    "min_steps": MIN_STEPS,
    "min_signals": MIN_SIGNALS,
    "min_patterns": MIN_PATTERNS,
    "min_pitfalls": MIN_PITFALLS,
    "min_done_when": MIN_DONE,
    "min_summary_chars": MIN_SUMMARY,
    "min_words": MIN_WORDS,
    "max_description_chars": MAX_DESCRIPTION,
}


def repo_root() -> Path:
    """Repository root: src/<package>/cli.py -> repo root."""
    return Path(__file__).resolve().parents[2]


def _report(issues: list[Issue], total: int, as_json: bool, title: str) -> int:
    bad = {issue.slug for issue in issues if issue.slug}
    valid = total - len(bad)
    if as_json:
        print(
            json.dumps(
                {
                    "pack": title,
                    "checked": total,
                    "valid": valid,
                    "passed": not issues,
                    "floors": FLOORS,
                    "issues": [
                        {"slug": i.slug, "rule": i.rule, "message": i.message}
                        for i in issues
                    ],
                },
                indent=2,
            )
        )
    else:
        print(f"{title}: {valid}/{total} skills valid")
        for issue in issues:
            print(f"  FAIL {issue}")
        if not issues:
            print(
                f"  ok  steps>={MIN_STEPS} signals>={MIN_SIGNALS} patterns>={MIN_PATTERNS} "
                f"pitfalls>={MIN_PITFALLS} words>={MIN_WORDS} refs canonical https"
            )
    return 0 if not issues else 1


def cmd_validate(args: argparse.Namespace) -> int:
    issues = validate_pack(PACK, SKILLS)
    root = Path(args.root) if args.root else repo_root()
    if not args.skip_files:
        for skill in SKILLS:
            path = root / "skills" / skill.slug / "SKILL.md"
            if not path.exists():
                issues.append(Issue(skill.slug, "file-missing", f"{path.relative_to(root)} missing"))
                continue
            if path.read_text(encoding="utf-8") != render_skill(PACK, skill):
                issues.append(
                    Issue(skill.slug, "file-drift", "SKILL.md on disk differs from the corpus render")
                )
    return _report(issues, len(SKILLS), args.json, PACK["name"])


def cmd_list(args: argparse.Namespace) -> int:
    skills = [
        skill
        for skill in SKILLS
        if (not args.tag or args.tag in skill.tags)
        and (not args.phase or skill.meta_get("phase") == args.phase)
    ]
    if args.json:
        print(
            json.dumps(
                [
                    {
                        "slug": s.slug,
                        "title": s.title,
                        "tags": list(s.tags),
                        "meta": s.meta,
                        "words": word_count(render_skill(PACK, s)),
                    }
                    for s in skills
                ],
                indent=2,
            )
        )
        return 0
    for skill in skills:
        phase = skill.meta_get("phase", "-")
        print(f"{skill.slug:44s} {phase:12s} {skill.title}")
    print(f"-- {len(skills)} skills")
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    for skill in SKILLS:
        if skill.slug == args.slug:
            print(render_skill(PACK, skill), end="")
            return 0
    print(f"unknown skill: {args.slug}", file=sys.stderr)
    return 1


def cmd_search(args: argparse.Namespace) -> int:
    terms = [t.lower() for t in args.terms]
    scored: list[tuple[int, Any]] = []
    for skill in SKILLS:
        haystack = " ".join(
            [skill.slug, skill.title, skill.summary, " ".join(skill.tags), " ".join(skill.steps)]
        ).lower()
        score = sum(haystack.count(term) for term in terms)
        if score:
            scored.append((score, skill))
    scored.sort(key=lambda pair: (-pair[0], pair[1].slug))
    for score, skill in scored[: args.limit]:
        print(f"{score:3d}  {skill.slug:44s} {skill.title}")
    if not scored:
        print("no matches")
        return 1
    return 0


def cmd_build(args: argparse.Namespace) -> int:
    root = Path(args.root) if args.root else repo_root()
    build_pack(root, PACK, SKILLS)
    issues = validate_pack(PACK, SKILLS)
    for skill in SKILLS:
        path = root / "skills" / skill.slug / "SKILL.md"
        if path.read_text(encoding="utf-8") != render_skill(PACK, skill):
            issues.append(Issue(skill.slug, "file-drift", "render mismatch"))
    bad = {i.slug for i in issues if i.slug}
    report = {
        "pack": PACK["name"],
        "version": PACK["version"],
        "expected_skills": PACK.get("expected_skills", len(SKILLS)),
        "checked": len(SKILLS),
        "valid": len(SKILLS) - len(bad),
        "passed": not issues,
        "floors": FLOORS,
        "issues": [
            {"slug": i.slug, "rule": i.rule, "message": i.message} for i in issues
        ],
    }
    results = root / "results"
    results.mkdir(parents=True, exist_ok=True)
    (results / "validation.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"built {len(SKILLS)} skills -> {root / 'skills'}")
    return 0 if not issues else 1


# ----------------------------------------------------------------- poc command


def build_pocplan(brief: dict[str, Any], top: int = 12) -> dict[str, Any]:
    """Turn a structured test brief into a phase-grouped PoC runbook.

    Vocabulary is aggregated across every field of the brief (weakness class,
    injection context, constraints and tags), so the plan reflects the whole
    authorization scope, not one line of the form.
    """
    title = str(brief.get("title", "untitled brief"))
    context = str(brief.get("context", "")).lower()
    weakness = str(brief.get("weakness", "")).lower()
    constraints = [str(c).lower() for c in brief.get("constraints", []) or []]
    tags = [str(t).lower() for t in brief.get("tags", []) or []]

    keywords: list[str] = []
    for value in (context, weakness, *constraints, *tags):
        for token in value.replace("-", " ").replace("_", " ").split():
            if token and token not in keywords:
                keywords.append(token)
    keywords = sorted(set(keywords))

    scored: list[tuple[int, int, Any]] = []
    for skill in SKILLS:
        haystack = " ".join(
            [skill.slug, skill.title, skill.summary, " ".join(skill.tags)]
        ).lower()
        haystack = haystack.replace("-", " ")
        score = sum(1 for k in keywords if len(k) > 2 and k in haystack)
        if score:
            phase = skill.meta_get("phase", "craft")
            if phase not in PHASE_ORDER:
                raise ValueError(f"{skill.slug}: unknown phase {phase!r}")
            scored.append((PHASE_ORDER.index(phase), score, skill))
    scored.sort(key=lambda t: (t[0], -t[1], t[2].slug))

    plan: list[dict[str, Any]] = []
    for phase_index, score, skill in scored[:top]:
        plan.append(
            {
                "phase": skill.meta_get("phase", "craft"),
                "slug": skill.slug,
                "title": skill.title,
                "match_score": score,
                "why": skill.summary,
                "steps": skill.steps,
            }
        )
    covered = {entry["phase"] for entry in plan}
    missing_phases = [p for p in PHASE_ORDER if p not in covered]
    return {
        "title": title,
        "context": context,
        "weakness": weakness,
        "constraints": constraints,
        "skills_total": len(SKILLS),
        "skills_matched": len(scored),
        "plan_steps": len(plan),
        "missing_phases": missing_phases,
        "plan": plan,
    }


def cmd_poc(args: argparse.Namespace) -> int:
    brief = json.loads(Path(args.brief).read_text(encoding="utf-8"))
    payload = build_pocplan(brief, top=args.top)
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0
    print(f"# PoC runbook - {payload['title']}")
    print(
        f"Context: {payload['context'] or '(unspecified)'}   "
        f"Skills matched: {payload['skills_matched']} of {payload['skills_total']}   "
        f"Plan steps: {payload['plan_steps']}"
    )
    if payload["missing_phases"]:
        print()
        print(
            "Thin coverage (no matched skill in these phases): "
            + ", ".join(payload["missing_phases"])
        )
    current = None
    for entry in payload["plan"]:
        if entry["phase"] != current:
            current = entry["phase"]
            print()
            print(f"## {current}")
        print()
        print(f"{entry['slug']}  (match {entry['match_score']})")
        print(f"  {entry['why']}")
        for idx, step in enumerate(entry["steps"], start=1):
            print(f"   {idx}. {step}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=PACK["name"],
        description=PACK["description"],
    )
    parser.add_argument("--version", action="version", version=f"{PACK['name']} {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("validate", help="run every corpus rule and check disk sync")
    p.add_argument("--json", action="store_true")
    p.add_argument("--root", default=None)
    p.add_argument("--skip-files", action="store_true", help="validate the corpus only")
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("list", help="list skills")
    p.add_argument("--tag", default=None)
    p.add_argument("--phase", default=None)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("show", help="print one SKILL.md")
    p.add_argument("slug")
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("search", help="rank skills by keyword")
    p.add_argument("terms", nargs="+")
    p.add_argument("--limit", type=int, default=10)
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("build", help="regenerate skills/, pack.json and results/")
    p.add_argument("--root", default=None)
    p.set_defaults(func=cmd_build)

    p = sub.add_parser(
        "poc",
        help="turn a structured test brief into a phase-grouped PoC runbook",
    )
    p.add_argument(
        "--brief", required=True, dest="brief", help="JSON file describing one authorized test brief"
    )
    p.add_argument("--top", type=int, default=12, help="maximum skills in the runbook")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_poc)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())