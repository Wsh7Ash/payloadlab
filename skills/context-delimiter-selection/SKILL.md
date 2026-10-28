---
name: context-delimiter-selection
description: "Choose the delimiters that terminate your input within its destination context so the proof ends where you intend instead of being consumed by surrounding syntax. Use when input lands inside structured syntax: markup, quoted strings, templates or queries"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [craft, context, encoding]
---

# Context Delimiter Selection

> Choose the delimiters that terminate your input within its destination context so the proof ends where you intend instead of being consumed by surrounding syntax

**Use when:** input lands inside structured syntax: markup, quoted strings, templates or queries

**Avoid when:** input is treated as opaque data with no syntax surrounding it

## Procedure

1. Identify the surrounding syntax at the destination: which characters open and close the surrounding construct.
2. Determine how many delimiter levels must be closed, since nested structures need matching closers.
3. Construct your input so it closes the surrounding construct cleanly before the demonstrative part.
4. Confirm the closing sequence survives the encoding layers you mapped earlier.
5. Verify by capture that the system parsed your structure rather than swallowing it as text.
6. Record the delimiter reasoning with the proof so a reviewer can see why those characters were chosen.

## Signals

- The demonstrative part of your input was absorbed into a surrounding string and never parsed.
- Quoting inside the destination differs from quoting in your request, so closers missed.
- A template layer adds its own delimiters on top of the transport's, adding another level to close.
- The proof works in one field but not an identically themed field with different surrounding syntax.

## Patterns

**1. Delimiter line**

```text
context=html-attribute open=quote close=quote levels=1 chosen=close-then-demonstrate verified=capture
```

**2. Nesting note**

```text
outer=template-literal inner=quoted-string closers-needed=2 supplied=2 result=parsed-as-structure
```

**3. Field contrast**

```text
field=search quoted=yes works=close-then-marker field=path quoted=no works=different-close note=syntax-differs
```

## Pitfalls

- Guessing delimiter syntax from a similar field instead of the one actually under test.
- Closing one level when the destination nests two, so the structure still consumes your input.
- Ignoring encoding on the closing characters, which may alter them before they arrive.
- Assuming success without a capture proving the destination parsed the structure as intended.

## Done when

- Surrounding syntax and its nesting levels are documented for the destination field.
- Chosen closers are confirmed to survive the transformation path.
- A capture proves the destination parsed your structure rather than absorbing it as text.

## References

- [OWASP - cross-site scripting prevention cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [CWE - weakness catalog](https://cwe.mitre.org/)
