---
name: out-of-band-callback-observation
description: "Use a callback channel you control to observe effects the response cannot show, with correlation that ties each callback back to the exact request that caused it. Use when the effect you must demonstrate is not visible in the synchronous response"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [observe, evidence, oast]
---

# Out of Band Callback Observation

> Use a callback channel you control to observe effects the response cannot show, with correlation that ties each callback back to the exact request that caused it

**Use when:** the effect you must demonstrate is not visible in the synchronous response

**Avoid when:** the response itself carries the evidence and no external observation is needed

## Procedure

1. Provision a callback endpoint you own, unique to this test so its traffic is unambiguous.
2. Embed the unique correlation token in the proof so each callback maps to one request.
3. Baseline the endpoint first, confirming zero unrelated traffic before execution.
4. Execute the proof and wait within a declared window rather than polling indefinitely.
5. Match each callback to its token, recording source, time and any request details observed.
6. Retire the endpoint after the test so later traffic cannot be mistaken for test evidence.

## Signals

- The callback endpoint already has traffic before your test, so hits cannot be attributed to it.
- No correlation token was embedded, so a hit proves little beyond that something reached you.
- Callbacks arrive from unexpected sources, which may be unrelated scanners you must not claim.
- The endpoint stays live after testing, and later traffic pollutes the evidence record.

## Patterns

**1. Baseline**

```text
endpoint=cb.example token=lab-118 pre-test-hits=0 window=baseline-15m status=clean
```

**2. Callback**

```text
time=09:14:22 token=lab-118 source=observed-path=/ fetch=1 attribution=to-request-4471
```

**3. Retirement note**

```text
endpoint=cb.example retired=2026-10-27 post-retire-hits=ignored note=recorded-as-out-of-scope
```

## Pitfalls

- Claiming a callback that carried no correlation token, which cannot be tied to your request.
- Skipping the baseline, so pre-existing scanner traffic reads as proof.
- Leaving the endpoint live, letting later unrelated hits muddy a clean record.
- Reporting callbacks from third parties that probed you independently of the test.

## Done when

- A per-test callback endpoint exists with a baseline of zero traffic before execution.
- Every claimed callback correlates to a token embedded in a specific request.
- The endpoint is retired and post-retirement traffic is excluded from evidence.

## References

- [OWASP - testing guidance for out-of-band verification](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
