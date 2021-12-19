import read_puzzle
from math import copysign
from itertools import zip_longest


def parse_endpoint(vent_lines):
    raw_endpoints = vent_lines.split(" -> ")
    endpoints = [
        tuple(int(x) for x in endpoint.split(",")) for endpoint in raw_endpoints
    ]
    return endpoints


def parse_lines(line_endpoints):
    difference = [
        line_endpoints[0][0] - line_endpoints[1][0],
        line_endpoints[0][1] - line_endpoints[1][1],
    ]
    width = max(line_endpoints[0][0], line_endpoints[1][0])
    depth = max(line_endpoints[0][1], line_endpoints[1][1])
    line_map = [[0 for x in range(width + 1)] for y in range(depth + 1)]
    # if (difference[0] or difference[1]) and not (difference[0] and difference[1]):
    current_point = [line_endpoints[0][0], line_endpoints[0][1]]
    while difference[0] != 0 or difference[1] != 0:
        line_map[current_point[1]][current_point[0]] = 1
        if difference[0] != 0:
            current_point[0] -= int(copysign(1, difference[0]))
            difference[0] -= int(copysign(1, difference[0]))
        if difference[1] != 0:
            current_point[1] -= int(copysign(1, difference[1]))
            difference[1] -= int(copysign(1, difference[1]))
    line_map[current_point[1]][current_point[0]] = 1
    return line_map


def merge_maps(maps_list):
    if len(maps_list) == 1:
        return maps_list[0]
    else:
        single_map = maps_list.pop(0)
        merged_maps = merge_maps(maps_list)
        outer_zipped = list(zip_longest(single_map, merged_maps, fillvalue=[]))
        zipped_map = []
        for zipped_line in outer_zipped:
            inner_zipped = list(
                map(lambda x: x[0] + x[1], zip_longest(*zipped_line, fillvalue=0))
            )
            zipped_map.append(inner_zipped)

        return zipped_map


def count_overlaps(vent_map):
    overlaps = 0
    for line in vent_map:
        for point in line:
            if point > 1:
                overlaps += 1
    return overlaps


# Begin options
use_example = False
# End options
puzzle_path = read_puzzle.make_puzzle_path(use_example, 5)
raw_puzzle = read_puzzle.get_puzzle_input(puzzle_path)
line_endpoints = [parse_endpoint(line) for line in raw_puzzle]
vent_maps = []
for endpoints in line_endpoints:
    vent_maps.append(parse_lines(endpoints))
merged_vent_map = list(merge_maps(vent_maps))
print(count_overlaps(merged_vent_map))
