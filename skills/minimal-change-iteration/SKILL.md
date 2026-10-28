---
name: minimal-change-iteration
description: "Refine the proof by changing one element per iteration, so you learn which part actually mattered instead of arriving at a working blob nobody can explain. Use when the first proof attempt works but contains elements whose contribution is unknown"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [craft, rigor, iteration]
---

# Minimal Change Iteration

> Refine the proof by changing one element per iteration, so you learn which part actually mattered instead of arriving at a working blob nobody can explain

**Use when:** the first proof attempt works but contains elements whose contribution is unknown

**Avoid when:** the proof is already a single change against a control

## Procedure

1. Start from the working proof and list each element it contains: fields, headers, values and sequence.
2. Change or remove exactly one element and rerun under identical conditions.
3. Record whether the observation persists, which tells you whether that element was load-bearing.
4. Keep the removal if the proof still works, and restore it if the proof breaks.
5. Repeat until no further reduction keeps the demonstration alive.
6. Document which elements were essential, since those define the actual mechanism of the weakness.

## Signals

- The proof works but includes fields that seem unrelated to the claim.
- Several elements were changed at once between attempts, so attribution is already lost.
- The reduced proof is smaller and reproduces more reliably than the original.
- Nobody can say which part of the proof is doing the work, including you.

## Patterns

**1. Iteration log**

```text
removed=extra-header result=still-works removed=field-b result=still-works removed=field-a result=fails keep=field-a
```

**2. Minimal form**

```text
input=one-field value=marker change=one-vs-control result=demonstrated elements-essential=[field-a]
```

**3. Attribution**

```text
load-bearing=field-a contributor=field-b optional=extra-header implication=mechanism-involves-field-a
```

## Pitfalls

- Removing elements in bulk, which destroys attribution and can break a working proof.
- Stopping at a working state instead of a minimal one, leaving the mechanism unexplained.
- Never re-testing the reduced form from clean state, so the reduction itself is unverified.
- Assuming an optional element is decorative when it actually gates the behavior.

## Done when

- No element can be removed while the demonstration still works.
- Each discarded element has a recorded note on its contribution.
- Essential elements are identified, which localizes the mechanism for the report.

## References

- [OWASP - testing guidance for minimal reproduction](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
