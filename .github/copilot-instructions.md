# Copilot Instructions for this Repository

## Build, test, and lint commands

This repository does not currently define a runnable build/test/lint toolchain.

- There is no `Makefile`, `pyproject.toml`, `requirements.txt`, `package.json`, or CI workflow yet.
- There are no test files or test runner configuration files yet.

For now, use a syntax check on the current Python file:

```bash
python -m py_compile pacman.py
```

Once tests are added, prefer documenting both full-suite and single-test commands in this file.

## High-level architecture

The current codebase is in bootstrap state:

- `README.md` is minimal and does not define architecture.
- `QWEN.md` contains the intended future architecture for a Python + Pygame Pac-Man clone.
- `pacman.py` is currently a draft/pseudocode-style placeholder and is not runnable game logic.

Planned architecture direction from `QWEN.md`:

- `main.py`: entry point
- `game.py`: game loop and state transitions
- `pacman.py`: player movement and collision interactions
- `ghost.py`: ghost AI behavior
- `maze.py`: map representation and rendering
- `settings.py`: shared constants/configuration
- `assets/`: sprites and sounds

## Key conventions specific to this repository

- Treat `AGENTS.md` as the active repository convention source for structure, style, and workflow expectations.
- Keep implementation guidance consistent with the Python/Pygame plan in `QWEN.md` unless superseded by code or newer docs.
- Because the project is not yet implemented, prefer adding concrete commands/conventions only when corresponding files/tooling are actually committed.
- When introducing new top-level directories, update both `README.md` and `AGENTS.md` to keep project layout guidance in sync.
