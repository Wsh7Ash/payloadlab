---
name: side-effect-verification
description: "Verify effects through a second independent read rather than trusting the action's own response, so a claimed change is confirmed where the state actually lives. Use when the proof claims an action changed state somewhere in the system"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [observe, evidence, verification]
---

# Side Effect Verification

> Verify effects through a second independent read rather than trusting the action's own response, so a claimed change is confirmed where the state actually lives

**Use when:** the proof claims an action changed state somewhere in the system

**Avoid when:** the claim concerns a read with no state change involved

## Procedure

1. Identify where the claimed effect would be persisted: record, log, queue or downstream system.
2. Read that location through a different path than the one the action used to report success.
3. Confirm the effect's presence with the marker or identifier tied to this specific test.
4. Check that the effect is attributable to your test and not to concurrent activity.
5. Record the independent verification with both the action response and the confirming read.
6. If the second read does not confirm, downgrade the claim rather than trusting the first response.

## Signals

- Success is asserted from the action's own response, which is exactly what would lie if broken.
- The confirming read uses the same code path, so both could share the same failure.
- Concurrent activity could have produced the state you are attributing to your test.
- The effect is not visible where you expected, which may mean it did not persist at all.

## Patterns

**1. Verify line**

```text
action=create-status=200 independent-read=list endpoint marker-found=yes attribution=confirmed
```

**2. Same-path flag**

```text
action=read-back-via-same-endpoint verdict=independent-enough=no next=read-via-other-path
```

**3. Downgrade**

```text
action-reported=applied confirm-read=absent verdict=not-confirmed claim=downgraded-to-unconfirmed
```

## Pitfalls

- Believing an action's success response without any independent confirmation.
- Confirming through the same code path, which shares the failure you are trying to rule out.
- Attributing state produced by someone else's concurrent activity to your own test.
- Reporting an unconfirmed effect as applied because the request returned success.

## Done when

- The claimed effect is confirmed by a read through a path independent of the action.
- The confirming evidence carries the marker or identifier of this specific test.
- Lack of confirmation downgrades the claim rather than being rationalized away.

## References

- [OWASP - testing guidance for verification](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
