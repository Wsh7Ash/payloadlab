---
name: capture-logging-discipline
description: "Capture every request and response of the proof in order with timestamps, so the full sequence can be replayed and audited rather than reconstructed from memory afterward. Use when a proof spans several exchanges whose order and content constitute the evidence"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [observe, evidence, records]
---

# Capture Logging Discipline

> Capture every request and response of the proof in order with timestamps, so the full sequence can be replayed and audited rather than reconstructed from memory afterward

**Use when:** a proof spans several exchanges whose order and content constitute the evidence

**Avoid when:** a single self-contained exchange is the whole demonstration

## Procedure

1. Enable capture before the first request, so nothing runs unrecorded while you settle the tooling.
2. Record each exchange with sequence number, timestamp, request and full response.
3. Annotate which step each exchange corresponds to, tying capture to the written plan.
4. Keep failed attempts in the record rather than deleting them, since they explain your path.
5. Export the capture in a form a reviewer can read without your tooling installed.
6. Reconcile the capture against the plan at the end, confirming every planned step is present.

## Signals

- Evidence was assembled afterward from memory, which produces a story rather than a record.
- Failed attempts were deleted, leaving a sequence that hides how the result was reached.
- Captures lack ordering, so the sequence of dependent requests cannot be reconstructed.
- A planned step has no captured exchange, meaning something ran unrecorded.

## Patterns

**1. Capture row**

```text
seq=1 t=09:14:01 step=create status=200 seq=2 t=09:14:06 step=other-read status=200 signal=rows
```

**2. Reconcile**

```text
planned=5 captured=5 missing=0 extra=1 extra-note=one-diagnostic-retry kept-in-record=yes
```

**3. Export form**

```text
format=request-response-text tooling-agnostic=yes reviewer-external-deps=none status=portable
```

## Pitfalls

- Reconstructing the exchange sequence from memory after the fact.
- Deleting failed attempts, which removes the context a reviewer needs to judge your path.
- Capturing without ordering, making dependent steps impossible to replay.
- Leaving a planned step uncaptured, so its outcome rests on your assertion.

## Done when

- Every exchange is captured in order with timestamps and mapped to plan steps.
- Failed attempts remain in the record with their diagnosis.
- The capture exports in a form readable without your original tooling.

## References

- [ISO 29147 - vulnerability disclosure](https://www.iso.org/standard/72311.html)
- [NIST - audit and accountability guidance](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
