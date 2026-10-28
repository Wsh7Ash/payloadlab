---
name: error-message-interpretation
description: "Read error responses as data about internal behavior, separating what the error reveals from what it merely decorates, so failures inform the proof instead of derailing it. Use when the system returns an error during testing and its content may itself be informative"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [observe, debugging, signals]
---

# Error Message Interpretation

> Read error responses as data about internal behavior, separating what the error reveals from what it merely decorates, so failures inform the proof instead of derailing it

**Use when:** the system returns an error during testing and its content may itself be informative

**Avoid when:** errors are generic and carry no information relevant to the claim

## Procedure

1. Capture the error in full: status, headers, body and any structured detail the system returned.
2. Separate operational detail, stack frames, query fragments or paths from ordinary user-facing text.
3. Determine whether the error resulted from your input or from a condition you did not create.
4. Check whether the error itself leaks information, since disclosure in an error can be its own finding.
5. Use the error to refine your understanding of the path, then adjust the proof deliberately.
6. Record errors with the evidence, so a reviewer sees what the system actually returned.

## Signals

- An error returns internal detail such as a path, query fragment or stack frame.
- The error contradicts your assumption about the code path, which is useful correction.
- You are retrying blindly past an error whose message names the actual problem.
- Errors are discarded rather than captured, so the evidence omits the system's own response.

## Patterns

**1. Error row**

```text
status=500 detail=sql-syntax-near quote=fragment leak=internal-path classification=informational
```

**2. Cause split**

```text
cause=input-caused=yes cause=pre-existing=no implication=error-reveals-handling-of-my-input
```

**3. Use note**

```text
error=named-missing-field action=add-field-and-retry record=error-with-evidence=yes
```

## Pitfalls

- Discarding an error whose content is itself part of the evidence.
- Treating an error caused by your malformed input as a defect of the target.
- Retrying past an error without reading it, which repeats the same failure.
- Reporting internal detail without deciding whether its disclosure is itself the finding.

## Done when

- Errors are captured in full with operational detail separated from user-facing text.
- Cause is attributed to input or to pre-existing conditions deliberately.
- Any disclosure value in the error itself is assessed and recorded.

## References

- [OWASP - testing guidance for error handling](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog for information exposure](https://cwe.mitre.org/)
