import tkinter as tk
import random
from .maze_objects import Door, Agent, Obstacle

CELL_SIZE = 20
WALL_WIDTH = 2

class MazeGUI:
    def __init__(self, maze):
        self.maze = maze
        self.width = maze.width
        self.height = maze.height
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.width*CELL_SIZE, height=self.height*CELL_SIZE)
        self.canvas.pack()

        for y in range(self.height):
            for x in range(self.width):
                cell = self.maze.grid[x][y]
                x1 = x * CELL_SIZE
                y1 = y * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                if cell.object is not None:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="grey")
                    if isinstance(cell.object, Door):
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="D", fill="white")
                    elif isinstance(cell.object, Agent):
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="A", fill="white")
                    elif isinstance(cell.object, Obstacle):
                        obstacle = random.randint(1, 3)
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")
                        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(obstacle), fill="black")
                else:
                    if cell.walls["top"]:
                        self.canvas.create_line(x1, y1, x2, y1, width=WALL_WIDTH)
                    if cell.walls["right"]:
                        self.canvas.create_line(x2, y1, x2, y2, width=WALL_WIDTH)
                    if cell.walls["bottom"]:
                        self.canvas.create_line(x1, y2, x2, y2, width=WALL_WIDTH)
                    if cell.walls["left"]:
                        self.canvas.create_line(x1, y1, x1, y2, width=WALL_WIDTH)

    def run(self):
        self.root.mainloop()
