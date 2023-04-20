import random

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}
        self.object = None

    def __str__(self):
        return f"({self.x}, {self.y})"

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell(x, y) for y in range(height)] for x in range(width)]

    def __str__(self):
        output = ""
        for y in range(self.height):
            for x in range(self.width):
                output += "  " if self.grid[x][y].walls["top"] else "__"
            output += "\n"
            for x in range(self.width):
                output += " " if self.grid[x][y].walls["left"] else "|"
                output += " " if self.grid[x][y].object is None else self.grid[x][y].object.symbol
                output += "|" if self.grid[x][y].walls["right"] else " "
            output += "\n"
        for x in range(self.width):
            output += "__"
        output += "\n"
        return output

class Object:
    def __init__(self, symbol):
        self.symbol = symbol

class Door(Object):
    def __init__(self):
        super().__init__("D")

class Agent(Object):
    def __init__(self):
        super().__init__("A")

class Wall(Object):
    def __init__(self):
        super().__init__("#")

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

    return maze


# maze = generate_maze(20, 20, 100)
# print(maze)
