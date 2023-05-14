import random
from .maze_objects import Cell, Door, Agent, Wall, Obstacle

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell(x, y) for y in range(height)] for x in range(width)]

    def __str__(self):
        output = "+"
        for x in range(self.width):
            output += "--+"
        output += "\n"

        for y in range(self.height):
            output += "|"
            for x in range(self.width):
                output += "  " if self.grid[x][y].walls["top"] else "__"
                output += "|" if self.grid[x][y].walls["right"] else " "
            output += "\n"

            output += "+"
            for x in range(self.width):
                output += " |" if self.grid[x][y].walls["bottom"] else "  "
            output += "\n"

        return output

def generate_maze(width, height, num_walls):
    maze = Maze(width, height)

    # place the door at the top left cell
    maze.grid[0][0].object = Door()

    # place the agent at the bottom right cell
    maze.grid[width-1][height-1].object = Agent()

    # randomly place the walls
    num_placed_walls = 0
    while num_placed_walls < num_walls:
        x, y = random.randint(0, width-1), random.randint(0, height-1)
        if maze.grid[x][y].object is not None or (x, y) == (0, 0) or (x, y) == (width-1, height-1):
            continue
        maze.grid[x][y].object = Wall()
        num_placed_walls += 1
    
    # randomly place obstacles
    for row in range(0, height):
        for col in range(0, width):
            if maze.grid[row][col].object is None:
                maze.grid[row][col].object = Obstacle()

    return maze