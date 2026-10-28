---
name: replay-package-assembly
description: "Assemble everything a third party needs to replay your proof from clean state, so verification does not depend on your environment, your memory or your continued availability. Use when a finding is complete and must be verifiable by someone other than you"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [report, evidence, reproduction]
---

# Replay Package Assembly

> Assemble everything a third party needs to replay your proof from clean state, so verification does not depend on your environment, your memory or your continued availability

**Use when:** a finding is complete and must be verifiable by someone other than you

**Avoid when:** the program accepts a description without replay expectations

## Procedure

1. List every input a replayer needs: preconditions, identities, exact requests and expected observations.
2. Order those inputs so the replay proceeds step by step with no hidden knowledge required.
3. Include the control alongside the test, since a replay cannot judge a delta it never sees.
4. State the expected observation for each step, so replay outcomes are checkable rather than intuitive.
5. Mark anything not replayable, such as environment state, with an explanation of the gap.
6. Hand the package to someone else if available, and fix wherever they stumbled.

## Signals

- The package assumes your tooling, your session state or a server configuration you did not record.
- Expected observations are described in prose instead of being stated per step.
- The control capture is missing, so a replayer cannot compute the delta that carries the claim.
- A known non-replayable element is present but not disclosed as a gap.

## Patterns

**1. Package list**

```text
contents=[preconditions,identity-map,ordered-requests,control-capture,expected-observations] gaps=[staging-flag]
```

**2. Step row**

```text
step=4 request=send-test expect=200-with-marker-if-vulnerable expect=403-or-empty-if-not
```

**3. Gap note**

```text
element=flag-state replayable=no reason=operator-set mitigation=describe-manual-setup disclosure=in-report
```

## Pitfalls

- Shipping a package that works only in your environment, which nobody else can rebuild.
- Omitting the control, so replay confirms arrival but cannot establish the delta.
- Leaving expected observations implicit, turning replay into interpretation.
- Hiding non-replayable elements instead of disclosing them, which a reviewer discovers anyway.

## Done when

- Every input needed for replay is present and ordered for step-by-step execution.
- Expected observations are stated per step with the control included.
- Non-replayable elements are disclosed with explanations of the gap.

## References

- [ISO 29147 - vulnerability disclosure](https://www.iso.org/standard/72311.html)
- [OWASP - testing guidance for reproducibility](https://owasp.org/www-project-web-security-testing-guide/)
