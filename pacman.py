""" pacman game
   - Define the maze layout using a 2D grid (list of lists or list of strings)
   - Use characters like: # for walls, . for pellets, o for power pellets, for empty spac
   - Create a Maze class that can draw the maze on screen
"""

WIDTH = 21
HEIGHT = 15


def generate_maze(w,h):
    maze = [["." for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            if x == 0 or y == 0 or x == w -1 or y == h - 1:
                maze[y][x] = '#'
            elif x % 4 == 0 and y % 2 == 0:
                maze[y][x] = '#'
                
    maze[1][1] = "P"
    return ["".join(row) for row in maze]
        
MAZE = generate_maze(WIDTH,HEIGHT)

def draw():
    for row in MAZE:
        print(row)
        
def main():
    draw()

if __name__ == "__main__":
    main()

