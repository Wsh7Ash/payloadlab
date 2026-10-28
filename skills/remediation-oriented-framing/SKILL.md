---
name: remediation-oriented-framing
description: "Frame the finding so its root cause and the class of fix are visible to the owning team, stating what you observed separately from what you infer about the cause. Use when the report is complete and you have a defensible read on the underlying cause"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [report, remediation, writing]
---

# Remediation Oriented Framing

> Frame the finding so its root cause and the class of fix are visible to the owning team, stating what you observed separately from what you infer about the cause

**Use when:** the report is complete and you have a defensible read on the underlying cause

**Avoid when:** you would be guessing at internal architecture you have no evidence for

## Procedure

1. State the observed behavior separately from your hypothesis about its cause, keeping the two apart.
2. Ground the hypothesis in evidence: which response, which signature, which pattern suggested it.
3. Describe the class of fix rather than prescribing an implementation you cannot see.
4. Name where else the same class likely appears, since one observed instance usually marks a pattern.
5. Flag any sibling path you already tested that shows the same behavior.
6. Keep the tone advisory so the owning team can translate guidance into their architecture.

## Signals

- Your suggested fix names internal modules or frameworks you have never seen.
- Observed behavior and hypothesized cause are stated as one thing, hiding what is inferred.
- A sibling endpoint shows the same behavior and your framing addresses only the first.
- Guidance reads as a demand for a specific implementation, which the team may rightly reject.

## Patterns

**1. Root cause**

```text
observed=read-without-ownership-check hypothesis=authorization-missing-at-data-layer evidence=200-with-other-rows
```

**2. Class note**

```text
fix-class=authorize-at-data-access likely-also=[list-endpoint,export-path] tested=list-also-fails=yes
```

**3. Tone check**

```text
phrasing=suggests-checking-not=must-implement advisory=yes overreach=no
```

## Pitfalls

- Presenting a speculative cause as settled fact, which the team may implement around blindly.
- Prescribing implementation details for code you cannot see.
- Addressing one instance when sibling endpoints you already touched show the same class.
- Omitting the second failing path you observed, so the fix ships incomplete.

## Done when

- Observation and hypothesis are stated separately with the hypothesis's evidence named.
- Guidance describes a fix class in advisory tone rather than an implementation.
- Sibling endpoints with the same behavior are listed as likely same-class instances.

## References

- [CWE - weakness catalog for class-level guidance](https://cwe.mitre.org/)
- [ISO 29147 - vulnerability disclosure](https://www.iso.org/standard/72311.html)
