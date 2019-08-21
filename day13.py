class Cart():
    def __init__(self, x, y, dir, turn):
        self.x = x
        self.y = y
        self.dir = dir # 'v'=0, '>'=1, '^'=2, '<'=3, makes it so any rotation is just a + or -
        self.turn = 0 # This depends on the rules at intersections
        self.dead = False

    def step(self, track):
        pass
    
