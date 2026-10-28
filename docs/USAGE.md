# Usage

## Setup

```shell
git clone https://github.com/Wsh7Ash/payloadlab.git
cd payloadlab
python -m pip install -e ".[dev]"
```

## Day-to-day commands

```shell
python -m payloadlab validate                # the 50/50 gate (exit 0 = all valid)
python -m payloadlab validate --json         # machine-readable report for CI
python -m payloadlab list                    # all 50 skills, one line each
python -m payloadlab list --phase craft      # only craft-phase skills
python -m payloadlab list --tag markers      # filter by tag
python -m payloadlab search marker control   # rank by keyword hits
python -m payloadlab show marker-payload-design  # full SKILL.md
python -m payloadlab build                   # regenerate skills/, pack.json, results/
```

## Turning a test brief into a PoC runbook

Write a small JSON brief (or copy `examples/demo-brief.json`):

```json
{
  "title": "Reflected input observed in an attribute context",
  "context": "html-attribute reflected search parameter",
  "weakness": "CWE-79 improper neutralization of input during web page generation",
  "constraints": ["authorized-scope only", "read-only evidence"],
  "tags": ["xss", "reflection"]
}
```

Then:

```shell
python -m payloadlab poc --brief examples/demo-brief.json
```

Output is a phase-ordered runbook: skills grouped under `## scope`,
`## hypothesis`, `## craft`, `## deliver`, `## observe`, `## report`, each
with matching steps and the reason it matched. Phases that matched nothing
are listed under *Thin coverage* so you can see what the runbook does not yet
address. Add `--json` for a machine-readable payload and `--top N` to cap
plan length.

Because `scope` leads `PHASE_ORDER`, permission and abort discipline always
surface before craft skills — the ordering encodes the pack's authorized-use
ethics rather than leaving them to the reader's discretion.

## Loading skills into agents

Each generated file `skills/<slug>/SKILL.md` has YAML front-matter
(`name`, `description`, `pack`, `version`, `category`, `tags`), which
agent skill loaders consume directly. Point your agent at the `skills/`
directory, or pick specific skills with `pack.json`'s per-skill paths and
SHA-256 digests.

## Regeneration discipline

Never edit `skills/`, `pack.json` or `results/` by hand. Edit the corpus
dicts in `src/payloadlab/corpus/part*.py`, run `python -m payloadlab build`,
then commit. The `test_committed_skills_match_corpus_render` test fails on
any drift, and CI rebuilds and diffs to prove it.

## Scope and ethics

payloadlab covers **authorized** proof-of-concept work: demonstration
discipline, evidence quality and reporting. It contains no exploitation
technique and no instruction to test anything outside an authorized scope.