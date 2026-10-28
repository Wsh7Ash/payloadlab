---
name: scope-record-keeping
description: "Keep one durable record linking permission, environment, identities and budget for each test, so any later question about what you were allowed to do has a single authoritative answer. Use when proof work spans sessions, people or programs and decisions live in scattered places"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [records, scope, process]
---

# Scope Record Keeping

> Keep one durable record linking permission, environment, identities and budget for each test, so any later question about what you were allowed to do has a single authoritative answer

**Use when:** proof work spans sessions, people or programs and decisions live in scattered places

**Avoid when:** a single one-off test runs and finishes inside one sitting

## Procedure

1. Open one record per test containing permission source, environment choice, identities and blast budget.
2. Append decisions as they are made with dates, rather than reconstructing them afterward from memory.
3. Attach the evidence for each decision: scope excerpt, confirmation reply, parity check, budget.
4. Keep the record versioned so a scope change during the test shows as a visible edit.
5. Store the record with the eventual finding so the report can cite its own authorization basis.
6. Review the record at close-out to confirm nothing tested exceeded what the record authorized.

## Signals

- Permission, budget and environment decisions live in three places and none references the others.
- You find yourself reconstructing why a choice was made last week from chat history.
- A scope edit arrived mid-test with no mechanism showing which earlier decisions it invalidated.
- The eventual report cannot cite the authorization that covered its own requests.

## Patterns

**1. Record header**

```text
test=poc-118 permission=policy-2026-10-27 env=staging budget=50-requests version=3
```

**2. Append line**

```text
date=2026-10-27 decision=switch-to-prod-trigger=staging-no-repro evidence=build-parity-note
```

**3. Close check**

```text
authorized=[all-executed-requests] exceptions=none verified-at-close=yes-by=you
```

## Pitfalls

- Reconstructing the record after the fact, which produces a story rather than evidence.
- Keeping decisions in chat where they cannot be versioned, diffed or cited.
- Failing to record mid-test scope edits, leaving earlier requests unverifiable against current rules.
- Storing the record away from the finding, so the report cannot cite its own authorization.

## Done when

- One record holds permission, environment, identities and budget with dated decision entries.
- Mid-test scope changes appear as versioned edits with their impact visible.
- Close-out review confirms no executed request exceeded what the record authorized.

## References

- [ISO 29147 - vulnerability disclosure](https://www.iso.org/standard/72311.html)
- [NIST - audit and accountability guidance](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
