---
name: severity-mapping-from-proof
description: "Derive severity from the program's own criteria applied to what you proved, with the reasoning written per factor, so the number arrives argued instead of asserted. Use when the submission requires a severity rating and the program publishes its scale"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [report, severity, rigor]
---

# Severity Mapping From Proof

> Derive severity from the program's own criteria applied to what you proved, with the reasoning written per factor, so the number arrives argued instead of asserted

**Use when:** the submission requires a severity rating and the program publishes its scale

**Avoid when:** the program assigns severity itself and asks you not to rate the finding

## Procedure

1. Read the program's severity definitions verbatim and note which factors each band keys on.
2. Score every factor from your evidence, including factors you could not test.
3. State the reasoning for each factor in one line, naming the evidence behind it.
4. Disclose untested factors and how you treated them instead of silently assuming the favorable case.
5. Compute the band from the factor scores rather than starting from a desired number.
6. Pre-write the strongest objection to your rating and answer it inside the rationale.

## Signals

- The rating was chosen first and factor scores assembled to justify it.
- Only impact was considered, while prerequisites and interaction factors went unexamined.
- You are citing a generic scale when the program publishes its own criteria.
- An untested factor is treated as favorable without disclosure anywhere in the submission.

## Patterns

**1. Factor line**

```text
vector=network auth=required interaction=none impact=high-data scope=same band=high all-tested=yes
```

**2. Untested**

```text
factor=scale-limits tested=no treatment=assumed-favorable disclosed=yes impact-on-band=none
```

**3. Objection**

```text
claim=requires-account reply=free-signup-suffices claim=bounded reply=37-records-evidenced-per-page
```

## Pitfalls

- Working backward from the band you want, which careful reviewers detect immediately.
- Scoring only impact while ignoring the other factors the band depends on.
- Assuming untested factors are favorable without saying so.
- Leaving the strongest counter-argument unaddressed, so triage raises it first.

## Done when

- Every severity factor is scored with a one-line rationale tied to evidence.
- Untested factors are disclosed with their assumed treatment.
- The strongest objection to the rating has a written answer in the rationale.

## References

- [FIRST - Common Vulnerability Scoring System](https://www.first.org/cvss/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
