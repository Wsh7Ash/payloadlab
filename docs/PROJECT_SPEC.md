# Project Spec — payloadlab

## Name

`payloadlab`

## Category

`defensive-security`

## Target user

Security researchers and agents who must turn an authorized finding into a proof a third party can audit — minimizing what the proof touches while maximizing what it demonstrates.

## Problem

A proof of concept is where most findings quietly fail: scope is assumed rather than confirmed, hypotheses are unfalsifiable, proofs carry elements nobody can explain, observations rest on impressions instead of captured deltas, and reports cannot be replayed by anyone but their author. The discipline that prevents this exists in scattered write-ups and hard-won conventions, but never as checkable, ordered skill files — so each proof re-derives it from scratch and the weak spots are never named, let alone enforced.

## Solution

A corpus of 50 unique, validated proof-of-concept authoring skills organised into the six phases of a proof arc, with a validator that enforces quality floors and a CLI that turns a structured test brief into a phase-ordered runbook with thin-coverage warnings.

## Core workflow

```text
author/edit corpus  ->  build  ->  skills/ + pack.json + results/
                                    |
                                    v
                          validate (50/50 gate)  ->  pytest  ->  CI
                                    |
                                    v
                       poc --brief brief.json -> ordered runbook
```

## Must-have features

- 50 unique skills with unique slugs and titles, covering scope, hypothesis, craft, deliver, observe, report.
- Validator with structural, strength and hygiene rules; exit `0` only at 50/50.
- Deterministic renderer; committed files proven in sync by tests.
- `poc` producing a phase-ordered runbook from a JSON test brief, with phase coverage gaps surfaced.

## Nice-to-have (explicitly out of scope for v1)

- Automated replay of a submitted proof.
- Integration with bug-bounty platforms for report submission.
- A scoring model beyond vocabulary matching.

## Acceptance tests

1. `validate` exits 0 and reports 50/50.
2. `pytest -q` passes 17 tests, including regeneration equality, drift detection and the poc round-trip.
3. `poc` — round-trips the checked-in example brief in `PHASE_ORDER`.
4. A generated build lands byte-identically in a clean temp directory.