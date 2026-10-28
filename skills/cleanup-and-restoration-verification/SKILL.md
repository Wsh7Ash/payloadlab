---
name: cleanup-and-restoration-verification
description: "Remove every trace your test created and verify the removal through an independent read, so the system ends in the state it was in before you began. Use when the proof created objects, sessions, files or records that must be removed"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [report, safety, records]
---

# Cleanup and Restoration Verification

> Remove every trace your test created and verify the removal through an independent read, so the system ends in the state it was in before you began

**Use when:** the proof created objects, sessions, files or records that must be removed

**Avoid when:** the proof was strictly read-only and created nothing anywhere

## Procedure

1. Walk the touch log and list every artifact the test created, modified or temporarily enabled.
2. Delete or restore each one using the inverse of the action that created it.
3. Verify removal through a read path independent of the deletion action itself.
4. Confirm no test objects remain visible to other users or operators as live content.
5. Retire any external resource the test used, such as a callback endpoint or test account.
6. Record cleanup completion with the verification reads, so closure rests on evidence.

## Signals

- Artifacts from the test still exist in the system after the test concluded.
- Deletion was confirmed by the delete action's own response rather than by a separate read.
- Test objects remain visible as live content to other users or to operators.
- An external resource such as a callback endpoint or account remains live and reachable.

## Patterns

**1. Cleanup row**

```text
artifact=test-order-4471 action=delete verified-by=independent-list-read status=absent
```

**2. Visibility**

```text
object=test-report-lab visible-to=other-users=no visible-to=operators=yes note=marked-then-removed
```

**3. Retirement note**

```text
resource=callback-endpoint status=retired resource=test-account-b status=disabled recorded=yes
```

## Pitfalls

- Trusting the delete action's success response without an independent confirming read.
- Leaving test objects visible as live content, which confuses operators and users later.
- Forgetting external resources such as endpoints or accounts, which outlive the session.
- Declaring cleanup complete without a record, so closure depends on memory.

## Done when

- Every artifact on the touch log is deleted or restored, each verified by an independent read.
- No test object remains visible as live content to users or operators.
- External resources are retired and cleanup completion is recorded with its verification reads.

## References

- [OWASP - testing guidance for cleanup](https://owasp.org/www-project-web-security-testing-guide/)
- [ISO 29147 - vulnerability disclosure](https://www.iso.org/standard/72311.html)
