class Cart():
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir # 'v'=0, '>'=1, '^'=2, '<'=3, makes it so any rotation is just a + or -
        self.turn = 0 # left=0, straight=1, right=2
        self.dead = False
        return

    def step(self, track):
        # Move forward
        if self.dir == 0:
            self.y += 1
        elif self.dir == 1:
            self.x += 1
        elif self.dir == 2:
            self.y -= 1
        elif self.dir == 3:
            self.x -= 1

        # Change direction if need be
        if track == '\\':
            self.dir = (self.dir + 1) % 4
        elif track == '/':
            self.dir = (self.dir + 3) % 4
        elif track == '+':
            if self.turn == 0:
                self.dir = (self.dir + 3) % 4
            # If it's 1, you don't turn
            elif self.turn == 2:
                self.dir = (self.dir + 1) % 4

            self.turn = (self.turn + 1) % 3

        return


def part1():
    return


def part2():
    return


print (part1())
print (part2())
    
