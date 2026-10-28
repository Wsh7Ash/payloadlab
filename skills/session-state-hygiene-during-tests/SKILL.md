---
name: session-state-hygiene-during-tests
description: "Control cookies, tokens and cached state during the proof so the identity you think you are testing is the identity actually being tested, run after run. Use when the proof depends on a specific role, account or session boundary"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [deliver, setup, rigor]
---

# Session State Hygiene During Tests

> Control cookies, tokens and cached state during the proof so the identity you think you are testing is the identity actually being tested, run after run

**Use when:** the proof depends on a specific role, account or session boundary

**Avoid when:** the test is unauthenticated and no session state exists to manage

## Procedure

1. Identify every state carrier your proof touches: cookies, tokens, local storage and server-side sessions.
2. Reset or isolate that state before each run so the identity under test is unambiguous.
3. Verify which identity the server actually saw, from the response rather than from your client's assumption.
4. Separate the two sides of a boundary test into distinct clean sessions with no shared carriers.
5. Watch for state leaking between runs through caches or reuse of an earlier client instance.
6. Record the session setup with the evidence so a reviewer knows which identity produced which response.

## Signals

- The response reflects a different identity than the one you intended to test with.
- Cookies from an earlier run persisted into this one, contaminating the session under test.
- Both sides of a boundary test shared a token or cookie, collapsing the boundary you meant to probe.
- Client-side state was reused, so the server never saw a genuinely fresh session.

## Patterns

**1. Session row**

```text
run=test identity=user-a carrier=cookie-session verified-by=response-echo state=fresh-shared-carriers=no
```

**2. Leak flag**

```text
cookie=stale-from-run-3 observed-in=run-4 effect=response-shows-user-c action=reset-client-state
```

**3. Pair hygiene**

```text
side-a=client-1 token=tok-a side-b=client-2 token=tok-b shared=none boundary=preserved
```

## Pitfalls

- Trusting the client's idea of who is logged in instead of the server's response.
- Reusing a client instance across runs, which silently carries cookies and tokens forward.
- Sharing a token between the two sides of a boundary test, which collapses the boundary.
- Reporting a session-dependent result without recording which session produced it.

## Done when

- Every state carrier is identified, reset and verified per run.
- The server-observed identity is confirmed from the response for each run.
- The two sides of a boundary test run in distinct sessions with no shared carriers.

## References

- [OWASP - session management cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [CWE - weakness catalog for session handling](https://cwe.mitre.org/)
