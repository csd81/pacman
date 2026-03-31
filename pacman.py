"""
pacman game   v0.1
"""

from dataclasses import dataclass, field
import pygame
import random

WIDTH = 21
HEIGHT = 15


@dataclass
class GameState:
    width: int = WIDTH
    height: int = HEIGHT
    maze: list[str] = field(init=False)
    pacman_x: int = 1
    pacman_y: int = 1
    ghost_x: int = 19
    ghost_y: int = 13
    score: int = 0
    lives: int = 3

    def __post_init__(self):
        self.maze = generate_maze(self.width, self.height)

    def can_move(self, x: int, y: int) -> bool:
        if x < 0 or y < 0 or y >= self.height or x >= self.width:
            return False
        return self.maze[y][x] != "#"

    def move_pacman(self, dx: int, dy: int) -> None:
        nx = self.pacman_x + dx
        ny = self.pacman_y + dy
        if abs(dx) + abs(dy) != 1:
            return
        if self.can_move(nx, ny):
            self.pacman_x = nx
            self.pacman_y = ny
        if self.can_move(nx, ny):
            self.pacman_x = nx
            self.pacman_y = ny
            self.eat_pellet()

    def move_ghost(self):
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = self.ghost_x + dx, self.ghost_y + dy
            if self.can_move(nx, ny):
                self.ghost_x = nx
                self.ghost_y = ny
                break

    def eat_pellet(self) -> None:
        x, y = self.pacman_x, self.pacman_y
        if self.maze[y][x] == ".":
            self.score += 10
            row = self.maze[y]
            self.maze[y] = row[:x] + " " + row[x + 1 :]


def generate_maze(w, h):
    maze = [["." for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            if x == 0 or y == 0 or x == w - 1 or y == h - 1:
                maze[y][x] = "#"
            elif x % 4 == 0 and y % 2 == 0:
                maze[y][x] = "#"
    maze[1][1] = " "
    return ["".join(row) for row in maze]


def draw_state_pygame(screen, state):
    cell = 40
    wall_color = (20, 20, 20)
    pellet_color = (255, 255, 255)
    pacman_color = (100, 100, 255)
    ghost_color = (200, 200, 200)

    screen.fill((50, 50, 50))
    
    for y in range(state.height):
        for x in range(state.width):
            ch = state.maze[y][x]
            px, py = x * cell, y * cell

            if ch == "#":
                pygame.draw.rect(screen, wall_color, (px, py, cell, cell))
            elif ch == ".":
                pygame.draw.circle(
                    screen, pellet_color, (px + cell // 2, py + cell // 2), 4
                )
    pygame.draw.circle(
        screen,
        pacman_color,
        (state.pacman_x * cell + cell // 2, state.pacman_y * cell + cell // 2),
        cell // 2 - 4,
    )
    pygame.draw.circle(
        screen,
        ghost_color,
        (state.ghost_x * cell + cell // 2, state.ghost_y * cell + cell // 2),
        cell // 2 - 4,
    )
    font = pygame.font.SysFont(None, 32)
    hud = font.render(
        f"Score: {state.score}   Lives: {state.lives}", True, (255, 255, 255)
    )
    screen.blit(hud, (10, 10))


def main():
    pygame.init()
    screen = pygame.display.set_mode((840, 600))
    state = GameState()
    clock = pygame.time.Clock()
    running = True
    frame_count = 0

    ghost_move_delay = 4

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            state.move_pacman(0, -1)
        if keys[pygame.K_s]:
            state.move_pacman(0, 1)
        if keys[pygame.K_a]:
            state.move_pacman(-1, 0)
        if keys[pygame.K_d]:
            state.move_pacman(1, 0)
        if keys[pygame.K_q]:
            running = False

        frame_count += 1
        if frame_count % ghost_move_delay == 0:
            state.move_ghost()

        pacman_pos = (state.pacman_x, state.pacman_y)
        ghost_pos = (state.ghost_x, state.ghost_y)

        if pacman_pos == ghost_pos:
            state.lives -= 1
            state.pacman_x, state.pacman_y = 1, 1
            state.ghost_x, state.ghost_y = 19, 13
        if pacman_pos == ghost_pos:
            state.lives -= 1
            if state.lives <= 0:
                state.lives = 0
                running = False
            else:
                state.pacman_x, state.pacman_y = 1, 1
                state.ghost_x, state.ghost_y = 19, 13
         
        draw_state_pygame(screen, state)
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()


if __name__ == "__main__":
    main()
