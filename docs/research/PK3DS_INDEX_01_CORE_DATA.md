# pk3DS Index 01 — Generation VI core data structures

## Scope and evidence state

This is the first source-level index of `kwsch/pk3DS` for Generation VI. It records what the public implementation does; it is **not** direct observation of this repository's retail Pokémon X target because no local retail image is available.

Pinned upstream revision reviewed:

- repository: `kwsch/pk3DS`
- branch: `master`
- commit: `6daaca934ca2284a73ab743bf89c848c57cd9de1`
- commit date: `2026-02-27`

Evidence class: **A — public implementation evidence**.

Any path, count, offset, or semantic name below must remain implementation-backed/reference evidence until independently cross-checked or later verified against a lawful target.

## 1. Game selection and high-level initialization

Source: `pk3DS.Core/Game/GameConfig.cs`

pk3DS currently distinguishes its extracted game layouts with file-count constants:

| pk3DS game family | file count used by `GameConfig` |
| --- | ---: |
| XY | 271 |
| ORAS demo | 301 |
| ORAS | 299 |

This is a pk3DS classification heuristic, **not a retail ROM fingerprint** and not evidence that every regional/revision build has an identical unpacked-file count.

For Generation VI, `GameConfig` initializes:

- personal data,
- level-up learnsets,
- game text,
- move data,
- evolution data,
- game information.

The implementation reports GARC version 4 for both XY and ORAS.

### Important XY / ORAS move-container difference

`InitializeMoves()` treats the games differently:

- XY: each file in the `move` GARC is parsed directly as a `Move6` record.
- ORAS: file 0 of the `move` GARC is additionally unpacked as a `Mini` container with magic/name `WD`, and the contained files are parsed as `Move6` records.

This difference requires independent format documentation; do not assume the XY move archive layout applies to ORAS.

## 2. pk3DS logical GARC map

Source: `pk3DS.Core/Game/GARCReference.cs`

`GARCReference` converts a three-digit logical file number into `a/<hundreds>/<tens>/<ones>` and labels selected paths by purpose. The mappings below are **pk3DS labels and mappings**, not yet retail-verified by this project.

### XY mapping used by pk3DS

| logical name | number | pk3DS path |
| --- | ---: | --- |
| `encdata` | 012 | `a/0/1/2` |
| `trdata` | 038 | `a/0/3/8` |
| `trclass` | 039 | `a/0/3/9` |
| `trpoke` | 040 | `a/0/4/0` |
| `move` | 212 | `a/2/1/2` |
| `eggmove` | 213 | `a/2/1/3` |
| `levelup` | 214 | `a/2/1/4` |
| `evolution` | 215 | `a/2/1/5` |
| `megaevo` | 216 | `a/2/1/6` |
| `personal` | 218 | `a/2/1/8` |
| `item` | 220 | `a/2/2/0` |
| `gametext` | 072 | `a/0/7/2` + language-relative offset |
| `storytext` | 080 | `a/0/8/0` + language-relative offset |

Other currently named XY resources in this table include `movesprite`, map resources, wallpaper, title screen, and normal/super Maison Pokémon/trainer resources.

### ORAS mapping retained for comparison

| logical name | number | pk3DS path |
| --- | ---: | --- |
| `encdata` | 013 | `a/0/1/3` |
| `trdata` | 036 | `a/0/3/6` |
| `trclass` | 037 | `a/0/3/7` |
| `trpoke` | 038 | `a/0/3/8` |
| `move` | 189 | `a/1/8/9` |
| `eggmove` | 190 | `a/1/9/0` |
| `levelup` | 191 | `a/1/9/1` |
| `evolution` | 192 | `a/1/9/2` |
| `megaevo` | 193 | `a/1/9/3` |
| `personal` | 195 | `a/1/9/5` |
| `item` | 197 | `a/1/9/7` |
| `gametext` | 071 | `a/0/7/1` + language-relative offset |
| `storytext` | 079 | `a/0/7/9` + language-relative offset |

The obvious path-number shifts are one reason XY and ORAS must not share an assumed archive map.

### Language-relative paths

pk3DS marks `gametext` and `storytext` as `LanguageVariant`. `GameConfig` applies the selected language integer as a relative GARC-number offset. This is implementation evidence that language is a data-selection axis in the tool. The exact retail language-index meaning and per-market equality must be independently audited before we use this mapping as a canonical region/language table.

## 3. Pokémon personal data

Sources:

- `pk3DS.Core/Structures/PersonalInfo/PersonalInfoXY.cs`
- `pk3DS.Core/Structures/PersonalInfo/PersonalInfoORAS.cs`
- `pk3DS.Core/Structures/PersonalInfo/PersonalTable.cs`

### Record sizes

| format | record size |
| --- | ---: |
| XY | `0x40` bytes |
| ORAS | `0x50` bytes |

`PersonalTable` explicitly selects `PersonalInfoXY` for XY and `PersonalInfoORAS` for ORAS/ORAS demo.

### XY fields exposed by pk3DS

The implementation maps at least:

- `0x00..0x05`: HP, Attack, Defense, Speed, Special Attack, Special Defense,
- `0x06..0x07`: type 1 / type 2,
- `0x08`: catch rate,
- `0x09`: evolution stage field,
- `0x0A..0x0B`: packed EV yield plus an additional bit interpreted by pk3DS,
- `0x0C..0x11`: three held-item slots,
- `0x12`: gender field,
- `0x13`: hatch cycles,
- `0x14`: base friendship,
- `0x15`: experience growth group,
- `0x16..0x17`: two egg groups,
- `0x18..0x1A`: three abilities,
- `0x1B`: escape rate,
- `0x1C..0x1D`: alternate-form stats index,
- `0x1E..0x1F`: form sprite field,
- `0x20`: form count,
- `0x21`: color plus two sprite-related bits,
- `0x22..0x23`: base EXP,
- `0x24..0x25`: height,
- `0x26..0x27`: weight,
- `0x28..0x37`: TM/HM compatibility bitfield,
- `0x38..0x3B`: type-tutor compatibility bitfield,
- `0x3C..0x3F`: explicitly left unknown by pk3DS.

### ORAS extension

`PersonalInfoORAS` inherits the XY field model and expands the record to `0x50` bytes. It adds four `0x04`-byte `SpecialTutors` bitfield groups at:

- `0x40..0x43`,
- `0x44..0x47`,
- `0x48..0x4B`,
- `0x4C..0x4F`.

This is a concrete public-implementation difference between XY and ORAS.

## 4. Move data

Source: `pk3DS.Core/Structures/Moves/Move6.cs`

pk3DS models a Generation VI move record as `0x22` bytes.

Fields exposed by the implementation include:

- type,
- quality,
- damage category,
- power,
- accuracy,
- PP,
- priority,
- minimum/maximum hit count,
- inflicted effect/status identifier and probability/duration,
- turn range,
- critical stage,
- flinch value,
- effect-sequence ID,
- recoil,
- healing behavior,
- target,
- three stat identifiers,
- three stat-stage values,
- three stat-effect probabilities,
- 32-bit `MoveFlag6` field.

Offsets are directly encoded in `Move6.cs`; field semantics should be cross-checked with an independent implementation before becoming project-canonical names.

## 5. Level-up learnsets

Source: `pk3DS.Core/Structures/Learnset.cs`

`Learnset6` expects data length divisible by four. Each ordinary record is:

- signed 16-bit move ID,
- signed 16-bit level.

The writer terminates the list by writing a 32-bit `-1` sentinel. The implementation derives the ordinary entry count as `(data length / 4) - 1`.

XY and ORAS both use `Learnset6` in `GameConfig`, though their GARC path numbers differ.

## 6. Evolution data

Source: `pk3DS.Core/Structures/Gen6/Evolutions.cs`

`EvolutionSet6` is modeled as:

- `8` slots,
- `6` bytes per slot,
- total `0x30` bytes.

Each slot is three little-endian 16-bit fields:

1. method,
2. argument,
3. resulting species.

The implementation deliberately keeps the meaning of `Argument` generic because it can represent level, item, move, or other method-dependent values.

## 7. Trainer data

Source: `pk3DS.Core/Structures/Gen6/TrainerData6.cs`

The same class contains an explicit XY/ORAS header distinction.

### XY header handling

- `Format`: 8-bit,
- `Class`: 8-bit.

### ORAS header handling

- `Format`: 16-bit,
- `Class`: 16-bit,
- then an additional 16-bit field (`uORAS` in the reader; writer currently emits zero).

Shared fields then include battle type, party count, four trainer-use items, AI, several unknown bytes, healer flag, money field, and prize field.

`Format` bits control whether individual party records include held items and/or explicit moves.

### Trainer Pokémon record exposed by pk3DS

The base portion contains:

- IV byte,
- packed PID/config byte,
- 16-bit level,
- 16-bit species,
- 16-bit form,
- optional 16-bit held item,
- optional four 16-bit move IDs.

pk3DS interprets the packed byte as containing ability, gender, and one additional bit. Exact bit semantics and unused values require independent verification.

## 8. Encounter handling — first index only

pk3DS has separate Generation VI wild-editor implementations:

- `pk3DS.WinForms/Subforms/Gen6/XYWE.cs`
- `pk3DS.WinForms/Subforms/Gen6/RSWE.cs`

`RSWE.cs` contains explicit commentary contrasting its encounter slot layout with an older XY layout. This strongly indicates the encounter subsystem must be audited separately for XY and ORAS.

Detailed encounter-table structure is intentionally deferred to a dedicated index rather than inferred from UI code in this first batch.

## 9. Mega Evolution audit lead

`pk3DS.WinForms/Subforms/Gen6/MegaEvoEditor6.cs` contains an ORAS-specific branch for species entry `384` (Rayquaza), warning that it uses a different activator and can Mega Evolve when it knows Dragon Ascent.

This is a valuable implementation lead for the later Mega Evolution subsystem audit; it is not yet a complete description of the retail battle-engine rule.

## Confidence / verification status

| Finding | Current project state |
| --- | --- |
| pk3DS source paths/classes listed above | Reviewed at pinned upstream commit |
| pk3DS XY/ORAS branching behavior | Public implementation evidence |
| record sizes and offsets as implemented | Public implementation evidence |
| pk3DS logical GARC purpose/path map | Public implementation evidence; retail verification pending |
| exact regional/revision equality | Unknown |
| exact retail hashes / byte matches | Unavailable |

## Next pk3DS batch

Audit separately:

1. XY and ORAS wild encounter table structures,
2. egg-move representation,
3. Mega Evolution table representation,
4. item structure,
5. Maison data,
6. game/story text references and language-index tables,
7. game-version and ExeFS/CRO mappings.

Keep each subsystem in a reviewable batch and cross-check with a second implementation before promoting names or semantics to project-canonical status.
