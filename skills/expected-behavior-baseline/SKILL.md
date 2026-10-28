---
name: expected-behavior-baseline
description: "Establish what the system should do under normal rules before testing, so the eventual observation is measured against a documented expectation instead of an intuition. Use when the correct behavior is assumed but not written down or verified anywhere"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [baseline, hypothesis, evidence]
---

# Expected Behavior Baseline

> Establish what the system should do under normal rules before testing, so the eventual observation is measured against a documented expectation instead of an intuition

**Use when:** the correct behavior is assumed but not written down or verified anywhere

**Avoid when:** the product documents this behavior precisely and you have confirmed the document matches

## Procedure

1. Find the authoritative statement of correct behavior: documentation, spec, policy or contract.
2. Confirm the documented rule against a live observation where possible, since docs drift too.
3. Capture the correct-case response under conditions identical to the planned test.
4. Record status, relevant body fields and headers so later comparison is concrete.
5. Note any variation the system legitimately produces, such as timestamps or identifiers.
6. Store the baseline with the test record so the comparison survives independent review.

## Signals

- Correct behavior is asserted from memory rather than from a document or a capture.
- Documentation and live behavior disagree, which is itself worth recording before testing.
- The baseline was captured under a different role or session than the test will use.
- Legitimate variation like timestamps was never noted, so later diffs will be noisy.

## Patterns

**1. Baseline line**

```text
case=request-own-order expect=200-with-own-fields captured=2026-10-27 role=member session=same-as-test
```

**2. Doc conflict**

```text
doc=says-404 live=200-with-empty-body verdict=documentation-stale record-anyway=yes
```

**3. Noise note**

```text
varies=[timestamp,request-id] constant=[status,body-shape] diff-rule=ignore-varies
```

## Pitfalls

- Asserting what should happen without capturing it, leaving the comparison subjective.
- Building the baseline under different conditions from the test, which invalidates the diff.
- Ignoring legitimate variation, so every diff looks like a finding.
- Trusting documentation that has never been checked against the live system.

## Done when

- Correct behavior is documented from an authoritative source and confirmed by a live capture.
- The baseline shares conditions with the planned test and its varying fields are noted.
- The capture is stored with the test record for later comparison.

## References

- [OWASP - testing guidance for baselines](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
