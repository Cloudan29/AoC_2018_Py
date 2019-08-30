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
        if track[self.y][self.x] == '\\':
            if self.dir == 0 or self.dir == 2:
                self.dir = (self.dir + 1) % 4
            else:
                self.dir = (self.dir + 3) % 4
        elif track[self.y][self.x] == '/':
            if self.dir == 0 or self.dir == 2:
                self.dir = (self.dir + 3) % 4
            else:
                self.dir = (self.dir + 1) % 4
        elif track[self.y][self.x] == '+':
            if self.turn == 0:
                self.dir = (self.dir + 1) % 4
            elif self.turn == 2:
                self.dir = (self.dir + 3) % 4

            self.turn = (self.turn + 1) % 3

        return

    def __lt__(self, cart):
        if self.y < cart.y:
            return True
        elif self.y == cart.y:
            if self.x < cart.x:
                return True

        return False

    def __gt__(self, cart):
        if self.y > cart.y:
            return True
        elif self.y == cart.y:
            if self.x > cart.x:
                return True

        return False

    def __eq__(self, cart):
        if not cart.dead:
            if self.y == cart.y and self.x == cart.x:
                return True
        
        return False

    def __repr__(self):
        return "Cart: " + str(self.x) + ", " + str(self.y)

    def __str__(self):
        if self.dir == 0:
            return 'v'
        if self.dir == 1:
            return '>'
        if self.dir == 2:
            return '^'
        if self.dir == 3:
            return '<'



def setup_track():
    track = []
    with open("inputs/day13.txt") as inp:
        for line in inp:
            track_row = []
            line = line.replace('\n', '')
            for c in line:
                track_row.append(c)
            track.append(track_row)

    carts = []
    for i in range(len(track)):
        for j in range(len(track[i])):
            if track[i][j] == '<':
                carts.append(Cart(j, i, 3))
                track[i][j] = '-'
            elif track[i][j] == '>':
                carts.append(Cart(j, i, 1))
                track[i][j] = '-'
            elif track[i][j] == '^':
                carts.append(Cart(j, i, 2))
                track[i][j] = '|'
            elif track[i][j] == 'v':
                carts.append(Cart(j, i, 0))
                track[i][j] = '|'

    return track, carts



def show_track(track, carts):
    display_track = []
    for row in track:
        display_track.append(row.copy())

    for cart in carts:
        display_track[cart.y][cart.x] = str(cart)

    for row in display_track:
        new_line = ''
        for c in row:
            new_line += c
        print (new_line)



def move_carts(track, carts):
    crash_locations = []
    i = 0
    while i < len(carts):
        crash = False
        j = 0
        carts[i].step(track)
        while j < len(carts):
            if i != j and carts[i] == carts[j]:
                crash_locations.append((carts[i].x, carts[i].y))
                carts[i].dead = True
                carts[j].dead = True
                if j < i:
                    i -= 1
                crash = True
                break

            j += 1

        if not crash:
            i += 1

    return crash_locations



def part1():
    track, carts = setup_track()

    while True:
        carts.sort()
        crash_locations = move_carts(track, carts)
        if len(crash_locations) > 0:
            break
        
    return crash_locations[0]



def part2():
    track, carts = setup_track()

    while True:
        carts.sort()
        move_carts(track, carts)
        carts = [cart for cart in carts if not cart.dead]
        if len(carts) == 1:
            break

    return (carts[0].x, carts[0].y)



print (part1())
print (part2())
    
