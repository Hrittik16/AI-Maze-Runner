class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}
        self.object = None

    def __str__(self):
        return f"Cell({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

class Door:
    def __init__(self):
        self.symbol = "D"

class Agent:
    def __init__(self):
        self.symbol = "A"

class Wall:
    def __init__(self):
        self.symbol = ""