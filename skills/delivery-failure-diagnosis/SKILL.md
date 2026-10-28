---
name: delivery-failure-diagnosis
description: "Diagnose a proof that did not fire by checking your own delivery first, distinguishing a broken proof from a genuine negative result before drawing any conclusion. Use when the demonstration produced no observation and you must decide what that means"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [deliver, debugging, rigor]
---

# Delivery Failure Diagnosis

> Diagnose a proof that did not fire by checking your own delivery first, distinguishing a broken proof from a genuine negative result before drawing any conclusion

**Use when:** the demonstration produced no observation and you must decide what that means

**Avoid when:** the observation occurred and the question is only how to present it

## Procedure

1. Check delivery first: did the request reach the server at all, with the intended framing and value.
2. Verify the marker and structure survived the path by capturing what actually arrived.
3. Confirm preconditions still held at execution time, since state may have changed since planning.
4. Check whether an abort condition or rate signal silently altered your own request.
5. Only after delivery, framing and preconditions check out, record the result as a genuine negative.
6. Record the diagnosis path with the outcome, so a negative result carries its own evidence.

## Signals

- No observation occurred and you are about to conclude the behavior does not exist.
- The request never reached the server because an endpoint changed since planning.
- Your marker arrived transformed, so searching for the original string could never match.
- A precondition lapsed between planning and execution, which delivery checks would reveal.

## Patterns

**1. Diagnose line**

```text
step=delivery check=server-saw-request yes step=marker check=arrived-transformed yes step=precondition check=held yes verdict=genuine-negative
```

**2. Self-fault**

```text
cause=request-never-sent cause=wrong-framing cause=precondition-lapsed implication=not-a-negative-result
```

**3. Record line**

```text
outcome=negative diagnosis-path=delivery-then-framing-then-preconditions all-passed=yes confidence=in-result
```

## Pitfalls

- Reporting a negative result from a proof that never actually arrived at the server.
- Checking only the absence of an error, when a request can fail silently and still return 200.
- Blaming the target for a delivery problem originating in your own client or constraints.
- Discarding the failed run instead of recording its diagnosis, so the same self-fault repeats.

## Done when

- Delivery, framing and preconditions are each verified before any negative is concluded.
- The diagnosis path and its checks are recorded alongside the outcome.
- Self-originating faults are distinguished from genuine negative results in the record.

## References

- [OWASP - testing guidance for result interpretation](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
