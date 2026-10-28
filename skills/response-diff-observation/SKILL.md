---
name: response-diff-observation
description: "Diff control and test responses field by field and read the difference rather than the noise, so the claim rests on a specific observable delta instead of an impression of wrongness. Use when two responses are captured and the difference between them is the thing being claimed"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [observe, evidence, diff]
---

# Response Diff Observation

> Diff control and test responses field by field and read the difference rather than the noise, so the claim rests on a specific observable delta instead of an impression of wrongness

**Use when:** two responses are captured and the difference between them is the thing being claimed

**Avoid when:** the observation is a state change on a shared object with no paired response

## Procedure

1. Capture both responses at identical fidelity: status line, headers and full body.
2. Normalize only the fields you know legitimately vary, such as timestamps and request identifiers.
3. Diff the normalized captures and list every remaining difference explicitly.
4. Attribute each difference to the single variable that changed, or mark it unattributed.
5. Select the differences that constitute the claim and label the rest as incidental.
6. Attach the labeled diff to the evidence so a reviewer reads the same delta you did.

## Signals

- You are reporting that a response looks wrong without naming which field carried the anomaly.
- Differences include fields that vary by design, which will distract a reviewer from the real one.
- Several fields differ and none is marked as the one the claim actually rests on.
- The captures were taken at different fidelities, so the diff includes artifacts of capture.

## Patterns

**1. Diff line**

```text
status=200/200 body.rows=own/other header.cache=miss/miss signal=body.rows noise=header.cache
```

**2. Attribute**

```text
difference=rows-content variable=target-id attribution=single-var status=attributed
```

**3. Label lines**

```text
claim-bearing=[body.rows] incidental=[timestamp,request-id] reviewer-note=read-claim-bearing-first
```

## Pitfalls

- Presenting an unlabeled diff, which forces the reviewer to find the claim themselves.
- Normalizing away the very field that carries the anomaly, deleting your own evidence.
- Comparing captures taken at different fidelities, so capture artifacts appear as findings.
- Reporting the impression rather than the delta, which cannot be audited or replayed.

## Done when

- Both captures exist at identical fidelity with only known noise normalized out.
- Every remaining difference is attributed or explicitly marked unattributed.
- Claim-bearing differences are distinguished from incidental ones in the attached diff.

## References

- [OWASP - testing guidance for response analysis](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
