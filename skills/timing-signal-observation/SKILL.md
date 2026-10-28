---
name: timing-signal-observation
description: "Measure time differences as evidence with enough repetitions and controls that the signal survives ordinary system noise instead of being an anecdote about one slow request. Use when the effect you must observe manifests in response time rather than content"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [observe, measurement, rigor]
---

# Timing Signal Observation

> Measure time differences as evidence with enough repetitions and controls that the signal survives ordinary system noise instead of being an anecdote about one slow request

**Use when:** the effect you must observe manifests in response time rather than content

**Avoid when:** the effect is directly observable and timing adds nothing

## Procedure

1. Define what timing difference you expect and roughly how large it should be.
2. Measure a control condition repeatedly to establish normal timing and its variance.
3. Measure the test condition with the same method, count and environment as the control.
4. Compare distributions rather than single samples, since one request proves nothing about time.
5. Rule out confounds: network path, cache state and server load differ between your conditions.
6. Report the measured difference with its sample counts and variability, never as a single number.

## Signals

- One slow request is being treated as evidence of a timing-based behavior.
- Control and test were measured under different network or cache conditions.
- The sample count is too small to separate the effect from ordinary noise.
- The expected effect size is smaller than the observed variance in your own control.

## Patterns

**1. Timing line**

```text
control n=30 median=42ms p90=61ms test n=30 median=188ms p90=240ms delta=+146ms
```

**2. Confound**

```text
control=warm-cache test=cold-cache implication=delta-may-be-cache action=equalize-then-rerun
```

**3. Noise note**

```text
expected-effect=50ms observed-variance=80ms verdict=below-noise-floor need=more-samples-or-bigger-effect
```

## Pitfalls

- Reporting a timing claim from a handful of samples, which noise will readily mimic.
- Letting cache or network conditions differ between control and test, which manufactures deltas.
- Quoting a single measurement as if it were a distribution.
- Claiming a delta smaller than the variance you already measured in the control.

## Done when

- Control and test are each measured with stated sample counts under equalized conditions.
- The comparison is distribution-based with variability reported.
- Confounders are either controlled or disclosed as limits on the claim.

## References

- [OWASP - testing guidance for timing analysis](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
