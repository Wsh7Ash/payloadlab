---
name: reflection-versus-execution-distinction
description: "Distinguish input that merely reappears from input the system actually interpreted, because the difference between echoing and processing is the difference between a weak and a strong claim. Use when your input returns in a response and the claim depends on whether it was processed"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [observe, rigor, interpretation]
---

# Reflection Versus Execution Distinction

> Distinguish input that merely reappears from input the system actually interpreted, because the difference between echoing and processing is the difference between a weak and a strong claim

**Use when:** your input returns in a response and the claim depends on whether it was processed

**Avoid when:** processing is unambiguous, such as an action completed with a recorded side effect

## Procedure

1. State explicitly what processing would look like for this context, not merely what a hit looks like.
2. Design a probe whose processed result differs unmistakably from its echoed form.
3. Capture the raw response bytes so encoding differences between echo and processing stay visible.
4. Check whether the system merely returned your input or transformed it according to its rules.
5. Report reflection alone as reflection, reserving the stronger claim for proven interpretation.
6. Escalate only when a second observation demonstrates processing beyond any echo explanation.

## Signals

- Your marker appeared verbatim, which proves arrival, not interpretation by the system.
- A plausible rival explanation says the input was simply echoed back unchanged.
- The claim language implies processing while the evidence shows only reappearing content.
- Raw bytes were never inspected, so an encoded echo and a processed value look identical.

## Patterns

**1. Probe line**

```text
input=marker-echo probe=marker-observed result=unchanged classification=reflection-only
```

**2. Process proof**

```text
input=structured-probe observed=parsed-and-transformed classification=interpreted-rival-echo-ruled-out
```

**3. Claim ladder**

```text
level-1=arrives level-2=reflected level-3=interpreted level-4=effective-each-level-needs-its-own-evidence
```

## Pitfalls

- Reporting a reflection as if it demonstrated processing, which a reviewer will knock down.
- Skipping raw-byte inspection, so echo and processing are indistinguishable in your capture.
- Jumping to the strongest claim on the first hit, without climbing the evidence ladder.
- Ignoring the echo rival, which is the most common innocent explanation for a visible hit.

## Done when

- Processing is defined in observable terms before the probe is sent.
- Raw captures distinguish an echoed value from a transformed one.
- The claim is stated at the level the evidence actually demonstrates, no higher.

## References

- [OWASP - testing guidance for interpretation](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
