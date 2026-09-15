# Decompilation Start

This document marks the transition from repository setup into active Pokémon X decompilation work.

## Operating rule

The retail game image is a local, read-only source. ROM/game-image binaries, decrypted title keys, console keys, and other sensitive key material are not committed to this repository. Reconstructed source, analysis, manifests, tooling, tests, metadata, and independently reproducible findings belong in Git.

## Phase 0 — Target identity

Before interpreting offsets or structures, every observation must be tied to an exact local target.

1. Preserve the original local target unchanged.
2. Record file size and SHA-256 with `tools/target_inventory.py`.
3. If an extracted working tree is used, inventory that tree separately.
4. Record region/language/revision/update information only when directly verified.
5. Never copy game-image bytes into a manifest.

Example:

```bash
python tools/target_inventory.py /path/to/local/pokemon-x.3ds \
  --label "Pokemon X / local target" \
  -o manifests/local-target.json
```

The generated manifest contains hashes and sizes only. Review it before committing; a committed manifest must not disclose private local paths or key material.

## Phase 1 — Container and executable map

For a verified local Nintendo 3DS target, document the hierarchy before decompiling code:

- outer game-image/container identity
- partitions/content units actually present in the verified target
- executable filesystem (ExeFS) inventory
- read-only filesystem (RomFS) inventory
- executable/code image identity and section mapping
- resource archives and compression layers encountered in the target

Do not assume that a layout from Pokémon Y, Omega Ruby, Alpha Sapphire, or another 3DS title is identical. Shared Generation VI structures may be promoted to a common model only after they are independently observed in each relevant target.

## Phase 2 — Executable reconstruction

Executable work proceeds from evidence rather than guessed names:

1. establish load/section boundaries and address conventions
2. record functions and cross-references with stable provisional identifiers
3. identify compiler/runtime/library patterns separately from game-specific code
4. rename symbols only when evidence supports the role
5. reconstruct functions into readable source while retaining provenance back to the observed binary range
6. add behavior or byte-level verification where practical

A source file is not considered matched merely because it looks plausible.

## Phase 3 — Game-data reconstruction

Resource work is tracked independently from executable code. Candidate categories include:

- GARC and other archive/container data
- BinLinker-style tables where actually observed
- scripts and event data
- Pokémon/battle/system parameters
- maps, field data, models, textures, animations, UI resources
- text/message resources and language variants
- audio metadata and resource indices

Existing format notes in `docs/formats/` are research aids, not proof that every documented format occurs at every path in this specific target.

## Generation VI comparison rule

Pokémon X is reconstructed as its own verified target first. Cross-title comparison then uses three explicit buckets:

- **XY common** — independently verified in both X and Y
- **Generation VI common** — independently verified across the relevant XY and ORAS targets
- **title/version specific** — observed only in one title, region, revision, language, or update state

This prevents later ORAS knowledge from being silently projected backward onto X.

## First concrete deliverable

The first active deliverable is a target inventory plus a top-level ExeFS/RomFS map from a verified local Pokémon X source. Once that exists, the project can select the first executable subsystem and the first data archive for source reconstruction.

## Current state

- Repository baseline: established
- ROM exclusion policy: established
- Target identity tool: added
- Target identity tests: added
- Verified Pokémon X retail target manifest: pending a locally available source
- ExeFS/RomFS map: pending a locally available source
- Executable source reconstruction: not yet started
