# scripts/ — the generation pipeline (single source of truth)

Three stages, run in order. Each stage owns distinct outputs; **do not let any stage write
another stage's files** (that caused a README clobber on 2026-07-08).

| Stage | Script | Reads | Owns / writes |
|---|---|---|---|
| 1. Data | `build_data.py` | live library API + `data/all-prompts.json` | `prompts.json`, `prompts.csv`, `PROMPTS.md`, `prompts/<slug>/README.md`, preview images |
| 2. Factor | `factor_prompts.py` | `prompts.json` | `systems/<slug>/` (style axis), `page-types/<cat>/` (structure axis) |
| 3. README | `gen_readme.py` | `prompts.json` + `data/all-prompts.json` | the auto-regions of `README.md` only (GALLERY / LEADERBOARD / STATS / synced-date) |

```bash
python3 scripts/build_data.py       # refresh the data
python3 scripts/factor_prompts.py   # re-factor systems/ + page-types/
python3 scripts/gen_readme.py       # refresh README auto-regions
```

## Ownership rules (why the clobber happened, so it doesn't again)
- **`README.md` is owned by `gen_readme.py`.** It surgically updates only the `<!-- X:START -->…<!-- X:END -->`
  regions; the hand-written positioning (hero, "3 ways to de-slop", registry/runtime, FAQ) is preserved.
  **Never regenerate the whole README** — `build_data.py`'s old whole-file README write is disabled on purpose.
- `LICENSE`, `CONTRIBUTING.md`, `TOPICS.md`, `.gitignore` are **hand-maintained**, not generated.
- The CI (`.github/workflows/sync.yml`) runs `gen_readme.py` on a schedule / on `prompts.json` change.

## Cross-session note
Two agent sessions built this repo in parallel (data layer + presentation layer). They're
complementary, but only if the ownership rules above hold. Coordinate handoffs via `loopbase`
before running generators.
