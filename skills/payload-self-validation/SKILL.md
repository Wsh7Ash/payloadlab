---
name: payload-self-validation
description: "Validate the proof against your own control before executing it live, catching malformed structure, dead markers and wrong assumptions while the cost of being wrong is still zero. Use when a proof is finished and about to be executed for real evidence"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [craft, validation, rigor]
---

# Payload Self Validation

> Validate the proof against your own control before executing it live, catching malformed structure, dead markers and wrong assumptions while the cost of being wrong is still zero

**Use when:** a proof is finished and about to be executed for real evidence

**Avoid when:** the proof was already executed and validated in this same session

## Procedure

1. Parse your own proof mechanically where possible: structure, encoding and required fields.
2. Run it against a control condition where the correct outcome is known in advance.
3. Confirm the marker is findable in your own captured output before searching for it elsewhere.
4. Check the proof against every constraint you recorded: length, context, delimiters and preconditions.
5. Fix any failure now, since a live execution that fails teaches you only that your prep was incomplete.
6. Record the self-validation result so the execution is known to have run against a checked proof.

## Signals

- The first live run fails on a structural error your own parser would have caught.
- The marker does not appear in your own control capture, so searching for it live will fail too.
- Constraints recorded earlier were never re-checked against the final proof version.
- You are about to execute a proof that has never been run in any form.

## Patterns

**1. Self-check**

```text
structure=parse-ok marker-found-in-control=yes constraints=all-passed verdict=cleared-to-run
```

**2. Control run**

```text
condition=control expected=no-hit observed=no-hit verdict=control-behaves-as-predicted
```

**3. Catch log**

```text
issue=unclosed-delimiter found-during=self-validation fixed-before-live=yes cost-avoided=one-wasted-run
```

## Pitfalls

- Using the first live execution as your validation, which burns a run and pollutes the evidence.
- Skipping the control check, so you cannot tell a broken proof from a negative result.
- Validating against stale constraints after the proof changed.
- Declaring self-validation complete while the marker has never actually been observed.

## Done when

- The proof parses, passes constraint checks and finds its marker in a control capture.
- The control run behaved as predicted.
- Self-validation results are recorded before live execution.

## References

- [OWASP - testing guidance for validation](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
