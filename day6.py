# Create dictionary containing all coordinates
coordinates = {}
with open("inputs/day6.txt") as inp:
    i = 0
    for line in inp:
        coordinates[i] = (int(line.split(", ")[0]), int(line.split(", ")[1]))
        i += 1


# Create the 2d list of tuples (closest_coordinate, sum_of_distances)
# Where -1 is a tie for closest_coordinate
AREA_SIZE = 1000
play_area = [[[-1, 0] for i in range(AREA_SIZE)] for j in range(AREA_SIZE)]
for i in range(len(play_area)):
    for j in range(len(play_area[i])):
        for k in coordinates:
            play_area[i][j][1] += abs(i - coordinates[k][0]) + abs(j - coordinates[k][1])


def part1():
    return


def part2():
    ans = 0
    for i in range(len(play_area)):
        for j in range(len(play_area[i])):
            if play_area[i][j][1] < 10000:
                ans += 1
    return ans


print (part1())
print (part2())