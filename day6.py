# Create dictionary containing all coordinates
coordinates = {}
with open("inputs/day6.txt") as inp:
    i = 0
    for line in inp:
        coordinates[i] = (int(line.split(", ")[0]), int(line.split(", ")[1]))
        i += 1


# Create the 2d list of tuples (closest_coordinate, sum_of_distances)
# Where -1 is a tie for closets_coordinate
AREA_SIZE = 500
play_area = [[[-1, 0] for i in range(AREA_SIZE)] for j in range(AREA_SIZE)]
for i in range(len(play_area)):
    for j in range(len(play_area[i])):
        distances = {}
        closest_coord = -1
        smallest_distance = 1000000

        for k in coordinates:
            distances[k] = abs(i - coordinates[k][0]) + abs(j - coordinates[k][1])
            play_area[i][j][1] += abs(i - coordinates[k][0]) + abs(j - coordinates[k][1])

        if not len(distances) != len(set(distances)):
            for k in distances:
                if distances[k] < smallest_distance:
                    smallest_distance = distances[k]
                    closest_coord = k

        play_area[i][j][0] = closest_coord


def part1():
    infinite_regions = [-1]
    for left in play_area[0]:
        if not left[0] in infinite_regions:
            infinite_regions.append(left[0])

    for right in play_area[-1]:
        if not right[0] in infinite_regions:
            infinite_regions.append(right[0])

    for col in play_area:
        if not col[0] in infinite_regions:
            infinite_regions.append(col[0])
        if not col[-1] in infinite_regions:
            infinite_regions.append(col[-1])

    region_sizes = {}
    for i in coordinates:
        if not i in infinite_regions:
            region_sizes[i] = 0

    for i in range(len(play_area)):
        for j in range(len(play_area[i])):
            if play_area[i][j][0] in region_sizes:
                region_sizes[play_area[i][j][0]] += 1

    largest_area = 0
    for i in region_sizes:
        if region_sizes[i] > largest_area:
            largest_area = region_sizes[i]

    return largest_area


def part2():
    return


print (part1())
print (part2())