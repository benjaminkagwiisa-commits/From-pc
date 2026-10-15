#Benjamin Kagwiisa

class Rover:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def __init__(self, terrain):
        self.mars = terrain
        self.x = 0
        self.y = 0

    def land(self, newX, newY):
        self.x = newX
        self.y = newY
        self.explore()

    def move(self, direction):
        if direction == Rover.UP:
            if self.y < self.mars.MAX_Y:
                self.y += 1

        elif direction == Rover.RIGHT:
            if self.x < self.mars.MAX_X:
                self.x += 1

        elif direction == Rover.DOWN:
            if self.y > 0:
                self.y -= 1

        elif direction == Rover.LEFT:
            if self.x > 0:
                self.x -= 1

        self.explore()

    def explore(self):
        discovery = self.mars.discover(self.x, self.y)
        print("                                    Discovered", discovery, "at", str(self.x) + "," + str(self.y))
