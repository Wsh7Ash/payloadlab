---
name: reproducibility-retest-before-submit
description: "Re-run the complete proof from written instructions on a later occasion before submitting, catching ambiguous steps and lucky conditions while you can still fix them. Use when a finding is finished and about to be submitted for the first time"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [report, reproduction, quality]
---

# Reproducibility Retest Before Submit

> Re-run the complete proof from written instructions on a later occasion before submitting, catching ambiguous steps and lucky conditions while you can still fix them

**Use when:** a finding is finished and about to be submitted for the first time

**Avoid when:** the proof has already been independently reproduced by a second party

## Procedure

1. Set the finished proof aside for a defined interval so accumulated context loses its grip.
2. Re-run it following only what is written, not what you remember doing.
3. Note every point where the written instructions were ambiguous, then fix the instructions.
4. Confirm the observation still occurs and still matches the evidence already captured.
5. Run from a second vantage point if possible, which exposes environment dependence quickly.
6. Record the retest result with the submission so consistency is a stated fact, not an implication.

## Signals

- The proof was written minutes after discovery, when every implicit step still felt obvious.
- Only one person has ever run it, which means unmeasured consistency rather than known consistency.
- The instructions reference state like the earlier request that no longer exists.
- A rerun succeeds only because you know an undocumented trick.

## Patterns

**1. Retest record**

```text
day=0 runs=2 fired=2 day=+1 runs=2 fired=2 vantage=second-network fired=yes consistency=4/4
```

**2. Ambiguity**

```text
step=4 unclear=the-earlier-request fix=specify-request-4471-with-id-substituted
```

**3. Record line**

```text
retest-result=consistent date=2026-10-27 note=attached-to-submission
```

## Pitfalls

- Re-running from memory, which tests recall rather than the written procedure.
- Treating a failed rerun as the finding disappearing rather than as an ambiguous instruction.
- Never testing a second vantage point, so environment dependence reaches triage unseen.
- Keeping consistency in your head instead of stating it in the submission.

## Done when

- The proof has been re-run from written instructions on a later occasion with the outcome recorded.
- A second vantage point has been tested where feasible.
- Ambiguities found during retest are fixed in the instructions themselves.

## References

- [ISO 29147 - vulnerability disclosure](https://www.iso.org/standard/72311.html)
- [OWASP - testing guidance for reproducible cases](https://owasp.org/www-project-web-security-testing-guide/)
