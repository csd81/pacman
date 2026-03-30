# Repository Guidelines

 ## Learning Mode (Persistent Rule)
 - The repository owner is a beginner programmer.
 - Copilot should act as a coding teacher: explain concepts, suggest next steps, 
review/debug user-written code, and help design tests.
 - Copilot must not directly modify project files; the user writes and runs all code.

## Project Structure & Module Organization
- This repo currently hosts `README.md`; as features arrive, keep source under `src/`, docs under `docs/`, and assets (sprites, data, configs) inside `assets/` or `data/` so collaborators know where to look.
- Mirror production code in `tests/` (e.g., `tests/game_engine.rs` alongside `src/game_engine.rs`) and document helper scripts in `scripts/` (e.g., `scripts/build.sh`).
- Update this guide and `README.md` whenever you introduce new top-level directories so the mental map stays accurate.

## Build, Test, and Development Commands
- `bash scripts/run.sh` (or similar) should start the app locally; describe its prereqs in `README.md` so teammates can reproduce it.
- `make build` (or `npm run build`) captures compilation/bundling once a toolchain exists; expand this section with actual commands once you choose a language stack.
- `make lint`/`npm run lint` and `make test`/`npm test` should be the verbs people run before committing; add short notes on what each command checks.

## Coding Style & Naming Conventions
- Favor 2-space indentation for JS/TS and 4 spaces for Python/C-style code; strip trailing whitespace and keep files UTF-8.
- Use descriptive camelCase or snake_case identifiers and name files in lower case with hyphens when multi-word (e.g., `pacman-controller.ts`).
- Run formatting via `prettier --write`, `black src/`, or similar configured tool before pushing; list the exact commands here once the toolchain is chosen.

## Testing Guidelines
- Pick a framework (pytest, jest, etc.) and keep tests near their modules. Name them `test_<feature>.py` or `feature.test.js` so the runner auto-discovers them.
- Document how to run tests (e.g., `python -m pytest tests/` or `npm test`) and mention coverage expectations or required fixtures.
- Store reusable fixtures under `tests/fixtures/` and avoid checking in large binaries—generate them in CI if needed.

## Commit & Pull Request Guidelines
- Commit in the imperative ("Add animation timing") and mention issue numbers if present; limit body lines to 72 characters for readability.
- PR descriptions should explain the change, link related issues, and list any manual verification steps or screenshots for UI changes.
- Tag reviewers by area (engine, art, docs) and rerun the relevant commands (`make test`, lint) before requesting review.

## Security & Configuration Tips
- Never commit secrets; keep environment variables in `.env` and add that file to `.gitignore` along with platform-specific caches.
- If new config keys are added later, document their purpose and default values in `README.md` or a dedicated `config/README.md` so contributors know how to set them up.
