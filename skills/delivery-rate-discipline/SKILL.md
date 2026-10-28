---
name: delivery-rate-discipline
description: "Send proof requests at a rate that neither distorts the system's behavior nor crosses into load, so results reflect normal processing and the test stays inside its declared budget. Use when the proof involves repeated requests, retries or a series of variants"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [deliver, safety, rigor]
---

# Delivery Rate Discipline

> Send proof requests at a rate that neither distorts the system's behavior nor crosses into load, so results reflect normal processing and the test stays inside its declared budget

**Use when:** the proof involves repeated requests, retries or a series of variants

**Avoid when:** the proof is a single request with no repetition at all

## Procedure

1. Estimate how many requests the proof needs and pace them so the total stays inside your blast budget.
2. Send at a rate approximating normal client behavior, since rate itself changes server behavior.
3. Watch for rate-limit responses, backpressure or errors that indicate you are changing the conditions.
4. Insert pauses between variants so each observation settles before the next is judged.
5. Stop and reassess if errors spike, since a stressed system produces observations that will not reproduce.
6. Record the pacing used with the evidence so a reviewer can replay at the same rhythm.

## Signals

- Error rates rise as you send faster, which means the system is reacting to your rate, not your input.
- Rate limiting engages and your later results reflect the limiter rather than the behavior under test.
- Variants fired back to back produced results that do not reproduce when sent alone.
- Total request count has crept past what your declared budget allows.

## Patterns

**1. Pace line**

```text
requests=18 pacing=1-per-2s limit-status=not-hit errors=0 verdict=conditions-stable
```

**2. Stress flag**

```text
burst=50-in-5s errors=spike verdict=rate-polluted-result action=slow-down-and-rerun
```

**3. Budget check**

```text
planned=20 sent=18 ceiling=50 remaining=32 status=inside-budget
```

## Pitfalls

- Firing variants in bursts, then reporting behavior the system only shows under load you created.
- Ignoring rate-limit signals, which silently rewrite the conditions of your later observations.
- Blaming the input for failures that were actually caused by your own pacing.
- Exceeding the declared request budget without recording the overrun.

## Done when

- Request count and pacing stay inside the declared blast budget.
- No rate-limit or stress signal distorted the observations.
- The pacing used is recorded with the evidence for replay.

## References

- [OWASP - testing guidance for safe scanning](https://owasp.org/www-project-web-security-testing-guide/)
- [CISA - coordinated vulnerability disclosure guidance](https://www.cisa.gov/coordinated-vulnerability-disclosure-process)
