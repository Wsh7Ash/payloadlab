# Security Policy

## Authorized use only

`payloadlab` is a knowledge corpus and planning tool for **authorized** proof-of-concept work: demonstrating a weakness in systems you own, or programs whose rules explicitly permit you to test them. The software itself performs no network requests — it renders, validates and plans locally.

The skills describe demonstration discipline: how to confirm permission, state a falsifiable hypothesis, build the smallest artifact that proves it, deliver it under control, observe the result as auditable evidence and report it so anyone can replay it. They contain no weaponized exploit material: the corpus teaches how to *prove* a weakness safely, not how to exploit one.

## Authorization leads every plan

The phase order itself encodes the discipline: `PHASE_ORDER` begins with `scope`, so a `poc` runbook always surfaces these skills before any craft skill:

1. `authorization-boundary-check` — permission is confirmed in writing before any request is built.
2. `blast-radius-budget` — the maximum effect of the proof is declared before execution.
3. `abort-criteria-and-kill-switch` — stop conditions and the means to stop are verified up front.
4. `non-destructive-test-design` — proofs demonstrate capability through reversible effects.

Craft and delivery skills only appear after the plan has passed through them.

## What this repository contains

- Methodology, checklists and diagnostic patterns for authorized proof-of-concept authoring and evidence handling.
- No exploit payloads, no credential harvesting techniques, no phishing material, no evasion or persistence guidance.
- No live target data, no credentials, no personal data. The example brief (`examples/demo-brief.json`) is synthetic.

## Reporting a vulnerability in this project

If you find a defect in `payloadlab` itself (for example, a validation bypass that lets a malformed skill pass the gate), please open a private security advisory on the repository or contact the maintainer through GitHub. Do not publish exploit details before a fix is available.

## Scope of this project's own testing

All tests run locally against the checked-in corpus and synthetic example files. No test sends traffic anywhere; the `poc` command operates on a checked-in JSON brief. Continuous integration runs the same local gates: validation, unit tests and an artifact-sync check.