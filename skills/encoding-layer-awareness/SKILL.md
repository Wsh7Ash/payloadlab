---
name: encoding-layer-awareness
description: "Track how many times your input is encoded and decoded between what you send and what arrives, so the proof targets the value that actually reaches the destination rather than the one you typed. Use when input travels through layers that encode, decode, escape or normalize values"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [encoding, craft, context]
---

# Encoding Layer Awareness

> Track how many times your input is encoded and decoded between what you send and what arrives, so the proof targets the value that actually reaches the destination rather than the one you typed

**Use when:** input travels through layers that encode, decode, escape or normalize values

**Avoid when:** the value passes through a single documented transport with no transformation

## Procedure

1. Map each transformation layer between sender and destination: transport encoding, escaping and parsing.
2. Write the value at every stage, showing exactly how it changes at each hop.
3. Identify where the destination performs its final decode, since that is the value it will interpret.
4. Construct the input so it reaches the destination in the intended form after all layers are applied.
5. Verify by observation: capture what arrived rather than trusting your transformation arithmetic.
6. Record the layer map with the proof so a reviewer can replay the reasoning.

## Signals

- Your test value arrived altered, which means an undocumented transformation exists somewhere in the path.
- You encoded twice for a single decode, so the destination saw the encoded form as literal content.
- A decoder normalizes aggressively, and equivalent encodings of your input behave differently.
- The proof works only for one of several equivalent encodings, which points at a specific layer.

## Patterns

**1. Layer map**

```text
send=url-encoded -> transport=raw -> server=url-decode -> sink=literal value-at-sink=as-typed verified=capture
```

**2. Double-encode**

```text
sent=double-encoded destination-decodes=once observed=encoded-literal implication=one-fewer-layer-needed
```

**3. Divergence**

```text
encoding-a=arrives-decoded encoding-b=arrives-encoded implication=differing-paths note=record-both
```

## Pitfalls

- Reasoning about encodings on paper and never checking what actually arrived.
- Encoding for the wrong layer, so your marker never matches during search.
- Assuming a single decode when the path contains two, which makes every attempt overshoot.
- Comparing encodings without noting they may take different paths through the system.

## Done when

- Every transformation layer is mapped with the value written at each stage.
- What arrived at the destination is verified by capture, not by calculation.
- The layer map is attached so the reasoning can be replayed independently.

## References

- [OWASP - input validation cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- [CWE - weakness catalog for encoding](https://cwe.mitre.org/)
