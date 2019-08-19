def part1():
    with open("inputs/day1.txt") as inp:
        sum = 0
        for line in inp:
            sum += int(line)

    return sum

# Brute force
def part2():
    sum = 0
    reaches = []
    while True:
        with open("inputs/day1.txt") as inp:
            for line in inp:
                sum += int(line)
                if sum in reaches:
                    return sum
                reaches.append(sum)

    
print (part1())
print (part2())