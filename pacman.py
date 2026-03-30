""" pacman game
   - Define the maze layout using a 2D grid (list of lists or list of strings)
   - Use characters like: # for walls, . for pellets, o for power pellets, for empty spac
   - Create a Maze class that can draw the maze on screen
"""

from dataclasses import dataclass, field
import pygame

WIDTH = 21
HEIGHT = 15


@dataclass
class GameState:
    width: int =WIDTH
    height: int = HEIGHT    
    maze: list[str] = field(init=False)
    pacman_x: int = 1
    pacman_y: int = 1
    score: int = 0
    lives: int = 3

    def __post_init__(self):
        self.maze = generate_maze(self.width, self.height)

    def can_move(self, x: int, y: int) -> bool:
        if x < 0 or y < 0 or y >= self.height or x>= self.width:
            return False
        return self.maze[y][x] != '#'

    def move_pacman(self, dx: int, dy: int) -> None:
        nx = self.pacman_x + dx
        ny = self.pacman_y + dy
        if abs(dx) + abs(dy) != 1:
            return
        if self.can_move(nx, ny):
            self.pacman_x = nx
            self.pacman_y = ny


        
def generate_maze(w,h):
    maze = [["." for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            if x == 0 or y == 0 or x == w -1 or y == h - 1:
                maze[y][x] = '#'
            elif x % 4 == 0 and y % 2 == 0:
                maze[y][x] = '#'                    
    return ["".join(row) for row in maze]
    
        
MAZE = generate_maze(WIDTH,HEIGHT)

    

def draw():
    for row in MAZE:
        print(row)

def draw_state_pygame(screen, state):
    cell = 40
    wall_color = (0, 0, 255)
    pellet_color = (255, 255, 255)
    pacman_color = (255, 255, 0)
 
    screen.fill((0, 0, 0))

    for y in range(state.height):
        for x in range(state.width):
            ch = state.maze[y][x]
            px, py = x * cell, y* cell

            if ch == "#":
                pygame.draw.rect(screen, wall_color, (px, py, cell, cell))
            elif ch == ".":
                pygame.draw.circle(screen, pellet_color, (px + cell //2, py + cell // 2), 4) 
    pygame.draw.circle(
        screen, pacman_color,
        (state.pacman_x * cell + cell // 2, state.pacman_y * cell + cell // 2), cell // 2 - 4
    )


def main():
    pygame.init()
    screen = pygame.display.set_mode((840,600))
    
    state = GameState()

    clock = pygame.time.Clock()
    running = True        
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: state.move_pacman(0, -1)            
        if keys[pygame.K_s]: state.move_pacman(0, 1)
        if keys[pygame.K_a]: state.move_pacman(-1, 0)
        if keys[pygame.K_d]: state.move_pacman(1, 0)
                
        draw_state_pygame(screen, state)
        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
