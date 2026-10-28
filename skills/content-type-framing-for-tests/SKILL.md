---
name: content-type-framing-for-tests
description: "Set and verify the content type framing every request, because the declared type decides how the body is parsed and a mismatch makes a correct proof look like a null result. Use when the request body carries structure the server must parse in a particular way"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [deliver, context, craft]
---

# Content Type Framing for Tests

> Set and verify the content type framing every request, because the declared type decides how the body is parsed and a mismatch makes a correct proof look like a null result

**Use when:** the request body carries structure the server must parse in a particular way

**Avoid when:** the endpoint documents a single content type you always send unchanged

## Procedure

1. Determine which content type the endpoint expects for the body you are sending.
2. Set it explicitly in your request rather than relying on client defaults.
3. Verify the server accepted the framing by its behavior, not only by the absence of an error.
4. Check whether an alternate content type routes to a different parser, which changes the destination context.
5. Keep the content type identical between control and test so framing never confounds the pair.
6. Record the chosen framing with the proof so replay uses the same parser path.

## Signals

- An implicit default content type was sent, and you cannot say which parser handled the body.
- The server responded to a type you did not declare, which means it guessed and you never checked.
- Control and test differ in content type, which confounds every difference in their responses.
- A different content type would reach a different parser, which you have not explored or disclosed.

## Patterns

**1. Frame line**

```text
sent=application/json parser=json-verified-by=structure-echo declared-explicitly=yes
```

**2. Parser contrast**

```text
type=json route=handler-a type=form route=handler-b implication=two-paths-one-untested
```

**3. Pair rule**

```text
control-type=json test-type=json match=yes confound=none
```

## Pitfalls

- Letting a client library choose the content type, which hides which parser actually ran.
- Changing framing between control and test, contaminating the comparison.
- Assuming a 200 means the body parsed as intended when the server may have ignored it.
- Testing one parser path while implying the claim covers every framing.

## Done when

- The content type is set explicitly and the server's parsing of it is confirmed by behavior.
- Control and test share identical framing.
- Other framings are either tested separately or disclosed as untested.

## References

- [OWASP - testing guidance for content types](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
