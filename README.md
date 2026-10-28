# payloadlab

**50 validated proof-of-concept authoring skills, plus a CLI that turns a test brief into a phase-grouped PoC runbook.**

## The problem

Writing a proof that survives review is its own discipline: deciding whether testing may proceed, stating a falsifiable hypothesis, building the smallest artifact that demonstrates it, delivering it under controlled conditions, observing the result as auditable evidence, and reporting it so a third party can replay everything. The methodology exists in scattered write-ups, but almost never as checkable, ordered skill files — so every new proof re-derives the same discipline from scratch, and the weak spots in it are never named.

## What this repo does

`payloadlab` is a corpus of **50 unique skills** organised into six phases of a proof-authoring arc — `scope → hypothesis → craft → deliver → observe → report` — with a validator that enforces structural and quality floors on every skill, and a CLI whose domain command (`poc`) turns a structured test brief into a phase-ordered runbook drawn from the corpus.

Every skill is a self-contained procedure with a summary, use/avoid guidance, a numbered procedure, observable signals, concrete patterns, pitfalls and completion criteria.

### Key features

- **50 skills, all validated**: `validate` enforces 6+ steps, 4+ signals, 3+ patterns, 3+ pitfalls, 180+ words, canonical `https` references, no placeholder tokens, no machine-local paths, unique slugs and titles, and byte-identical agreement with the files on disk.
- **`poc`**: turns a JSON test brief (context, weakness, constraints, tags) into a phase-ordered runbook, scoring the corpus against the brief's vocabulary and flagging phases with thin coverage.
- **`validate`**: the "50/50 valid" gate. Exits non-zero on any violation, with `--json` for CI.
- **`build`**: deterministically regenerates `skills/`, `pack.json` (SHA-256 per skill) and `results/`.
- **`list` / `show` / `search`**: browse and search the corpus locally, no network required. `list --phase` filters to one phase.
- **Zero runtime dependencies**: Python standard library only; `pytest` is the single dev dependency.

### Terminal example

```console
$ python -m payloadlab validate
payloadlab: 50/50 skills valid
  ok  steps>=6 signals>=4 patterns>=3 pitfalls>=3 words>=180 refs canonical https

$ python -m payloadlab poc --brief examples/demo-brief.json --top 24
# PoC runbook - Reflected input observed in an attribute context
Context: html-attribute reflected search parameter on a member-only page   Skills matched: 38 of 50   Plan steps: 24

## scope
  authorization-boundary-check  (match 1)
  ...
```

## Skill phases

| Phase | Count | Covers |
|---|---|---|
| `scope` | 8 | authorization checks, test identities, blast-radius budget, test data, environment choice, abort criteria, record keeping, non-destructive design |
| `hypothesis` | 8 | falsifiable statement, behavior baseline, input surface, sink context, preconditions, success criteria, rival explanations, variable isolation |
| `craft` | 9 | marker design and uniqueness, benign technique choice, minimal-change iteration, encoding layers, delimiters, length limits, legibility, self-validation |
| `deliver` | 8 | injection point selection, control pairing, channel routing, content-type framing, sequence ordering, rate discipline, session hygiene, failure diagnosis |
| `observe` | 8 | response diffing, out-of-band callbacks, reflection vs execution, error interpretation, timing measurement, side-effect verification, capture discipline, false-positive refutation |
| `report` | 9 | replay package, impact from evidence, redaction, severity mapping, remediation framing, retest, blind walkthrough, evidence indexing, cleanup verification |

## Scope and ethics

This pack is about **authorized** proof-of-concept work. It teaches demonstration discipline — what you may test, how to prove it minimally, how to observe and document the result. It contains no exploitation technique, no weaponized payload and no instruction to test anything outside an authorized scope.

## Install

```shell
python -m pip install -e ".[dev]"
```

## Usage

```shell
export PYTHONPATH=src                          # or install with pip -e
python -m payloadlab validate                  # the 50/50 gate
python -m payloadlab validate --json           # machine-readable, for CI
python -m payloadlab build                     # regenerate skills/, pack.json, results/
python -m payloadlab list --phase craft        # one phase
python -m payloadlab show marker-payload-design
python -m payloadlab search control evidence
python -m payloadlab poc --brief examples/demo-brief.json
python -m pytest -q                            # 17 passed
```

## Loading skills into agents

Each `skills/<slug>/SKILL.md` is a self-contained skill file with YAML front-matter, loadable by Claude Code, opencode, or any runtime that reads `SKILL.md` corpora. Copy the `skills/` directory into your agent's skills path, or consume `pack.json` as the index.

## Documentation

- [`docs/PROJECT_SPEC.md`](docs/PROJECT_SPEC.md) — what the pack is and is not
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — corpus, validator, renderer, CLI
- [`docs/USAGE.md`](docs/USAGE.md) — command-by-command walkthrough
- [`RESULTS.md`](RESULTS.md) — executed validation evidence

## License

MIT