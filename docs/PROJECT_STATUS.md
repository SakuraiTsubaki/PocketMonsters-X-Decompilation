# Project Status

**Current stage:** Active decompilation — Phase 0 target identification

This document tracks decompilation progress, target-version coverage, validation level, and the next major milestones.

## Version inventory

| Target | Region | Language | Revision / update | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| Pokémon X local retail target | TBD | TBD | TBD | Unverified | Exact source hash and revision are pending a locally available target |

## Progress

- [x] Establish repository policy and ROM/key exclusion rules
- [x] Add reproducible target identity/inventory tooling
- [x] Add regression tests for target inventory generation
- [ ] Establish authoritative version/revision inventory from verified local targets
- [ ] Document outer container, ExeFS, RomFS, and executable layout
- [ ] Map symbols, functions, and major subsystems
- [ ] Document game-data formats and resource containers as they are observed
- [ ] Reconstruct scripts, events, and behavior
- [ ] Reconstruct asset pipelines and metadata
- [ ] Add reproducible extraction/repacking tooling for verified formats
- [ ] Add automated verification where practical

## Validation levels

- **Unverified** — proposed or recorded but not independently checked.
- **Observed** — confirmed directly in a target build or extracted data.
- **Reproduced** — behavior or data can be recreated with documented steps.
- **Matched** — reconstructed output is verified against the intended target.

## Active workflow

1. Inventory the exact local Pokémon X target with `tools/target_inventory.py`.
2. Record region, language, revision, update state, size, and hashes without committing game bytes.
3. Produce the first ExeFS/RomFS and executable identity map.
4. Select one executable subsystem and one data archive for initial reconstruction.
5. Compare against Pokémon Y only after the corresponding X observations are recorded.

See [`DECOMPILATION_START.md`](DECOMPILATION_START.md) for the operating sequence and Generation VI comparison rules.

## Immediate milestone

The next milestone is a verified Pokémon X target manifest and top-level filesystem/executable map. Binary source material remains local and read-only; only hashes, metadata, reconstructed source, tooling, tests, and analysis are committed.
