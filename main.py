from maze_generator import generate_maze
from maze_generator import MazeGUI

maze = generate_maze(20, 20, 50)  # generate_maze(rows, columns, num_walls)
maze_gui = MazeGUI(maze)
maze_gui.run()
