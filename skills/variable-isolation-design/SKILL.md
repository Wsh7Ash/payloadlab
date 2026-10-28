---
name: variable-isolation-design
description: "Plan the proof so exactly one variable changes between control and test, making the difference attributable instead of leaving reviewers to guess which of several changes caused it. Use when the test involves multiple candidate inputs or conditions that could each affect the result"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [rigor, design, evidence]
---

# Variable Isolation Design

> Plan the proof so exactly one variable changes between control and test, making the difference attributable instead of leaving reviewers to guess which of several changes caused it

**Use when:** the test involves multiple candidate inputs or conditions that could each affect the result

**Avoid when:** a single input change with an obvious effect is all the proof requires

## Procedure

1. Identify every factor that could plausibly change the outcome in this test.
2. Choose the one factor your hypothesis concerns and fix everything else to identical values.
3. Run a control first: identical conditions with the factor in its normal state.
4. Change only the chosen factor and run the test, keeping captures from both runs.
5. If the result differs, attribute it to the single changed factor and say so explicitly.
6. If the result does not differ, vary one additional factor deliberately in a separate run rather than a combined one.

## Signals

- Control and test differ in more than one field, so any difference is confounded.
- No control run exists, leaving the observation unanchored to a normal-case capture.
- Several changes were made at once because each seemed necessary, which breaks attribution.
- The report claims causation from a comparison that varied multiple things.

## Patterns

**1. Isolation line**

```text
control=role=member,target=own-order test=role=member,target=other-order changed=target-id-only diff=status-200-vs-403
```

**2. Run record**

```text
run=control captured=09:14 run=test captured=09:16 all-else=identical attribution=single-factor
```

**3. Multi-change flag**

```text
changed=[id,header,cache-bust] verdict=confounded action=split-into-separate-runs
```

## Pitfalls

- Changing several variables because the run seemed more realistic that way.
- Skipping the control, so nothing anchors the comparison to normal behavior.
- Claiming causation from a confounded diff, which a careful reviewer will reject immediately.
- Combining a follow-up variable change into the same run instead of a separate one.

## Done when

- Exactly one factor differs between control and test, with both captures stored.
- The report attributes the observed difference to that single changed factor.
- Any additional factor was varied only in a separate, clearly labeled run.

## References

- [OWASP - testing guidance for controlled comparison](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
