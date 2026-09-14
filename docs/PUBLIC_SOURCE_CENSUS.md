# Public Source Census — Pokémon X

This repository currently assumes **no local retail ROM, CCI, CIA, RomFS, ExeFS, save dump, or extracted game asset is available**. Therefore the project must reconstruct knowledge from public documentation, public source code, preserved research, official information, and independently verifiable datasets.

This file is the master census for that work. A source being listed here does **not** mean every statement in it is correct. Claims are promoted into project documentation only after source-level review and, where possible, independent cross-checking.

## Canonical regional research policy — Japanese edition as comparison origin

This project performs an **exhaustive all-region investigation with the Japanese release as the comparison origin**.

- The Japanese edition is the project's baseline coordinate for names, text, data, presentation, assets, behavior, distribution history, and version-difference tables.
- This is a research convention, **not** an assumption that the Japanese build was necessarily released earlier, is always technically older, or is internally the source build for every asset.
- Every evidenced retail region, language configuration, revision, update, demo, distribution environment, and platform-service dependency must be inventoried rather than collapsed into a generic “international version.”
- Differences are recorded directionally as `Japanese baseline → target region/language/revision`, while version-exclusive gameplay differences such as X↔Y remain a separate comparison axis.
- A localization difference is not automatically a region difference, and a region difference is not automatically a ROM/data difference. Text selection, font resources, locale flags, title/update identifiers, packaging/manual material, distribution infrastructure, and executable/data changes must be classified separately.
- Shared byte-identical or behavior-identical material should be deduplicated in the research database while preserving every region/language/revision in provenance metadata.
- Japanese official terminology and Japanese in-game text are preserved as primary comparison fields; current official Korean terminology is used for Korean-facing documentation, with historical Generation VI Korean wording separately recorded when it differs.
- No regional build, language, revision, or patch may be declared identical to another without evidence. “Same as JP” is itself a finding that requires support.
- Public-source conclusions must retain an evidence state: observed in implementation, documented by an official/contemporaneous source, independently cross-confirmed, or provisional pending stronger evidence.

### Mandatory comparison dimensions

For every data domain where public evidence exists, the census must attempt to distinguish:

1. Japanese retail/base release.
2. Other retail regions and their title/update identities.
3. Every selectable or distributed language evidenced for Generation VI.
4. Version-exclusive X versus Y behavior/data.
5. Base revision versus every downloadable update revision.
6. Demo/trial/special-distribution builds where applicable.
7. Local wireless, Internet-service, event-distribution, and peripheral/service differences by territory and time period.
8. Packaging/manual/official-web differences when they document rules, terminology, features, or content not recoverable elsewhere.
9. Censorship, rating, legal, UI, font, text-layout, naming, audio, graphical, network, or event differences tied to territory or language.
10. Later corrections or terminology changes, without retroactively rewriting what the Generation VI build actually contained.

The regional census remains open until each investigated domain has an explicit matrix of **JP baseline / target region-language / revision / evidence / difference status / unresolved gaps**.

## Evidence classes

- **A — implementation evidence:** public source code that parses, writes, validates, emulates, or edits the relevant structure.
- **B — technical documentation:** reverse-engineering notes, platform documentation, file-format documentation, or research writeups.
- **C — structured preservation data:** event archives, save/entity format corpora, machine-readable datasets, text corpora, or preserved metadata.
- **D — official / contemporaneous reference:** official game sites, manuals, patch notes, developer interviews, Nintendo / Pokémon material.
- **E — secondary cross-check:** encyclopedias, wikis, databases, guides, research forum threads, and community documentation.

A ROM-derived assertion that is only supported by E-class material remains provisional.

## Core public reverse-engineering sources

| Source | Class | Main value | Gen VI relevance | Local policy |
|---|---|---|---|---|
| `kwsch/pk3DS` | A | GARC handling; Gen VI personal data, moves, learnsets, evolutions, trainers, encounters, marts, CRO-related editing | XY + ORAS | Treat source behavior as implementation evidence; audit license before copying code |
| `TeamEXR/shutan-dev-wiki` | B | Gen VI overview; GARC, BinLinker, LZ11, scripts, sequences, text/localization, battle, field, UI notes | XY-focused with Gen VI/ORAS coverage | Research reference only; verify uncertain/TODO claims elsewhere |
| `Rynbo/CTRMap` | A | Gen VI world/zone editing, collision, props, cameras, NPCs | XY + ORAS | Mine parsers/format definitions and cross-check with later forks |
| `hdent1232/CTRMap-F5` | A | Modern continuation with zone, trainer, script, geometry and collision validation; pawn script disassembly/assembly | strongest public ORAS world/script evidence; some XY support | High-priority audit; distinguish F5 discoveries from original CTRMap assumptions |
| `gdkchan/Ohana3DS-Rebirth` | A | BCH/model/texture/animation viewing and parsing | XY + ORAS graphics | Compare with SPICA and newer importers |
| `gdkchan/SPICA` | A | H3D/BCH serialization/deserialization | XY + ORAS 3D assets | Unlicense upstream is especially useful for independent implementation study |
| `sxrmss/n3ds_importer` | A | GFModel, GFMotion, GFTexture, BCH, PICA200 attributes and texture formats | explicitly covers XY/ORAS | Modern cross-check for graphics formats; note tested vs synthetic-only paths |
| `kwsch/PKHeX` | A/C | PK6/EK6, WC6, XY/ORAS save structures, legality and game-version handling | XY + ORAS | Primary public implementation source for save/entity/event formats |
| `projectpokemon/EventsGallery` + Project Pokémon Gen 6 gallery | C/E | preserved WC6/WC6FULL distributions and event metadata by language/region | XY + ORAS | Index metadata and hashes; do not blindly assume every archived card is complete or version-restricted |
| `abcboy101/poke-corpus` | C | standardized Pokémon text dump corpus and notes on XY-style text conventions | useful for text-format comparison | Do not republish bulk copyrighted game text; use format/metadata observations only unless licensing permits |

## Nintendo 3DS platform sources

| Source | Class | Main value | Use in this project |
|---|---|---|---|
| 3dbrew — NCCH / CXI / CFA | B | container layout, encryption regions, ExeFS/RomFS placement, flags | establish platform container model without a retail image |
| 3dbrew — RomFS / filesystem services / ExeFS / CRO pages | B | filesystem and executable-module structures | cross-check Project_CTR and emulator implementations |
| `3DSGuy/Project_CTR` (`ctrtool`, `makerom`) | A | reading/extracting and constructing NCCH, CXI/CFA/CCI/CIA, ExeFS, RomFS | executable reference for container parsing/reconstruction |
| `azahar-emu/azahar` (Citra lineage) | A | 3DS loader, filesystem, CRO/module, GPU and service behavior | platform-behavior reference when game-specific docs are incomplete |
| devkitPro `citro3d` / `tex3ds` | A/B | PICA200-facing texture formats, ETC1/ETC1A4, texture handling; documented LZ11 container type | graphics/compression cross-check independent of Pokémon tools |

## Official and game-behavior sources to inventory

The census must also locate and preserve metadata for:

- Pokémon/Nintendo official XY pages, manuals, announcements and support articles.
- Every XY update revision (1.0 through 1.5) and official changelog wording where recoverable.
- Official localization names for every supported language.
- Official strategy/reference material when it supplies facts not exposed elsewhere.
- Interviews and developer material describing engine, graphics, localization or design changes.

Secondary references such as Bulbapedia may be used to discover dates and claims, but official or contemporaneous sources should replace them wherever recoverable.

## Data domains that require separate source sweeps

The census is not complete until each of these domains has a source map and gap list:

1. 3DS container / NCCH / ExeFS / RomFS / update-title layout.
2. ARM11 `.code`, CRO modules, relocations, symbols and executable boundaries.
3. GARC, BinLinker and compression variants.
4. Text containers, character encoding, control codes, language tables and font resources.
5. Event/script bytecode, commands, native/engine function IDs, triggers and sequences.
6. Map zones, headers, area data, geometry, collision, props, cameras, NPCs and warp/trigger data.
7. Pokémon personal data, forms, stats, abilities, held-item slots, growth and compatibility flags.
8. Moves, learnsets, egg moves, evolution tables, TM/HM data and tutors.
9. Trainers, trainer classes, party formats, AI flags, rewards and battle types.
10. Wild encounters, hordes, fishing, Friend Safari and special encounters.
11. Items, shops, key items, berries, Mega Stones and item effects.
12. Battle engine behavior, type chart, abilities, weather, Mega Evolution and other Gen VI mechanics.
13. Graphics: GFModel/BCH/H3D, materials, textures, shaders, animations, UI images and icons.
14. Audio: BCSAR/BCH-related audio resources, sequences, banks, streams and cries.
15. Save structure, PK6/EK6, battle videos, Wonder Cards, Pokémon Link and online-related persisted data.
16. PSS, GTS, Wonder Trade, Battle Spot, O-Powers, Pokémon-Amie, Super Training and other network/UI systems.
17. Version, language, region and revision differences between X and Y.
18. Patch deltas from 1.0 to 1.5.
19. Unused, debug, inaccessible and leftover data documented by preservation/research communities.
20. Later Gen VII+ implementations that retain or transform Gen VI structures, used only as reverse cross-checks.

## Verification rules

- Never manufacture a ROM offset, GARC path, command ID, file count, hash or asset identity.
- Record whether a fact is **observed in public implementation**, **documented**, **cross-confirmed**, or **still provisional**.
- Prefer two independent implementations over one wiki statement.
- XY and ORAS must not be merged merely because both are Generation VI.
- X and Y differences must be recorded separately where known.
- Patch/revision-specific behavior must not be generalized to 1.0.
- Source code may be studied freely; code copied into this repository requires license compatibility review and attribution as applicable.
- Publicly available copyrighted game data is not automatically safe to mirror. Prefer metadata, format descriptions, checksums, tooling and independently written documentation.

## Current high-priority audit order

1. Fully index `pk3DS` Gen6 structures and game configuration mappings.
2. Fully index Project Shutan pages and mark incomplete/uncertain claims.
3. Diff original CTRMap against CTRMap-F5 for every Gen VI structure and command table.
4. Index PKHeX Gen6 save/entity/mystery-gift implementations.
5. Build graphics format crosswalk: Ohana3DS-Rebirth ↔ SPICA ↔ n3ds_importer ↔ citro3d/tex3ds.
6. Build 3DS platform crosswalk: 3dbrew ↔ Project_CTR ↔ Azahar.
7. Inventory Project Pokémon Gen VI event records by language, distribution type and game compatibility metadata.
8. Sweep official/archived XY material, patch history, localization and contemporaneous developer material.
9. Sweep secondary encyclopedias/forums only after implementation and official sources are indexed.

## Status

**Open-ended exhaustive census in progress.** Public research is distributed across many projects and historical posts, so completeness is measured by explicit domain coverage and a maintained gap list rather than by assuming any single search result set is exhaustive.