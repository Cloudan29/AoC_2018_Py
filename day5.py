import string

def part1(polymer):
    flag = True
    while flag:
        flag = False
        for i in range(len(polymer)-1):
            if polymer[i].isupper():
                if polymer[i+1] == polymer[i].lower():
                    polymer = polymer[:i] + polymer[i+2:]
                    flag = True
                    break
            else:
                if polymer[i+1] == polymer[i].upper():
                    polymer = polymer[:i] + polymer[i+2:]
                    flag = True
                    break

    return len(polymer)


def part2():
    low_alpha = string.ascii_lowercase
    high_alpha = string.ascii_uppercase
    lengths = []
    polymer = open("inputs/day5.txt").read()
    for _ in range(len(low_alpha)):
        lengths.append(part1(polymer.replace(low_alpha, '').replace(high_alpha, '')))
    return min(lengths)


print (part1(open("inputs/day5.txt").read()))
print (part2())