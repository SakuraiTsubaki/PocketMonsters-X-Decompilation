# Phase 4 — Function Boundary and Symbol Manifest

Phase 4 provides the normalized record format used when real ARM11 executable analysis begins for Pokémon X, Y, Omega Ruby, and Alpha Sapphire.

## Principle

Function boundaries and semantic names are separate claims. A function may be recorded as soon as an address and size are observed, while its neutral identifier remains `sub_XXXXXXXX`. A semantic rename is allowed only when evidence supports it.

## Tool

`tools/function_manifest.py` accepts a JSON function list and produces a deterministic manifest containing:

- start address and end address
- size
- symbol
- validation status (`provisional`, `observed`, `reproduced`, `matched`)
- evidence records
- overlap diagnostics
- optional text-segment coverage and out-of-range diagnostics

Example input:

```json
[
  {"address": "0x00123400", "size": "0x48"},
  {
    "address": "0x00123448",
    "size": "0x90",
    "symbol": "CandidateName",
    "status": "observed",
    "evidence": ["xref:caller_00123000", "string:verified-local-target"]
  }
]
```

The example name is intentionally generic and is not a claim about any Pokémon title.

## Promotion rule

1. Record independently observed function boundaries per exact title/revision.
2. Keep neutral provisional names until evidence supports a semantic rename.
3. Compare X↔Y and OR↔AS only after each side has its own manifest.
4. Promote identical or corresponding behavior to XY common, ORAS common, or Generation VI common only with direct cross-title evidence.

## Next step with real binaries

Once the verified local `.code` text segment is available, function-boundary discovery, call/xref extraction, strings/data references, and reconstructed source files can begin. Every reconstructed function should retain a link back to its exact observed address range and target identity.
