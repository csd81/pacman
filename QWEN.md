# Pac-Man Game Project

## Project Overview

This is a new/empty project directory intended for developing a **Pac-Man arcade game clone**. The project is in its initial state with only basic git initialization.

**Current Status:**
- Git repository initialized
- No source code implemented yet
- No dependencies or configuration files

**Intended Goal:**
Build a classic Pac-Man game featuring:
- Pac-Man character with keyboard controls
- Maze with pellets and power pellets
- Four ghosts with unique AI behaviors (Blinky, Pinky, Inky, Clyde)
- Scoring system and lives
- Win/lose conditions

## Technology Stack

| Technology | Purpose |
|------------|---------|
| **Python 3** | Programming language |
| **Pygame** | Game development library |

## Project Structure

```
pacman/
├── main.py           # Game entry point
├── game.py           # Main game loop and state
├── pacman.py         # Pac-Man character logic
├── ghost.py          # Ghost AI behaviors
├── maze.py           # Maze generation and rendering
├── settings.py       # Game configuration constants
├── assets/
│   ├── images/       # Sprites and graphics
│   └── sounds/       # Audio files
├── README.md
└── QWEN.md
```

## Building and Running

### Setup

```bash
# Install dependencies
pip install pygame
```

### Run the Game

```bash
python main.py
```

## Development Conventions

**To be established** when code is added. Recommended practices:

- Follow PEP 8 style guide for Python code
- Use type hints for function signatures
- Use docstrings for classes and functions
- Keep functions small and focused (single responsibility)
- Use constants in `settings.py` for game configuration
- Organize sprites using Pygame's sprite groups

## Next Steps

1. Create `settings.py` with game constants (screen size, colors, speeds)
2. Create `maze.py` with maze layout and rendering
3. Create `pacman.py` with Pac-Man character and movement
4. Implement collision detection
5. Create `ghost.py` with ghost AI behaviors
6. Create `game.py` with main game loop
7. Create `main.py` entry point
8. Implement scoring and game states
