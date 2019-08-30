addr = lambda registers, values : registers[values[2]] := registers[values[0]] + registers[values[1]]
def addi(registers, values):
    registers[values[2]] = registers[values[0]] + values[1]
def mulr(registers, values):
    registers[values[2]] = registers[values[0]] * registers[values[1]]
def muli(registers, values):
    registers[values[2]] = registers[values[0]] * values[1]
def banr(registers, values):
    registers[values[2]] = registers[values[0]] & registers[values[1]]
def bani(registers, values):
    registers[values[2]] = registers[values[0]] & values[1]
def borr(registers, values):
    registers[values[2]] = registers[values[0]] | registers[values[1]]
def bori(registers, values):
    registers[values[2]] = registers[values[0]] | values[1]
def setr(registers, values):
    registers[values[2]] = registers[values[0]]
def seti(registers, values):
    registers[values[2]] = values[0]


def part1():
    with open("inputs/day16a.txt") as inp:
        pass
    return


def part2():
    return


print (part1())
print (part2())