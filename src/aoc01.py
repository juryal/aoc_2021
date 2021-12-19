from collections import deque
import read_puzzle


def part_one(file):
    depthqueue = deque()
    increases = 0
    for line in file:
        depth = int(line.strip("\r\n"))
        depthqueue.append(depth)
        if len(depthqueue) == 2:
            if depthqueue[0] < depthqueue[1]:
                increases += 1
            depthqueue.popleft()
    return increases


def part_two(file):
    depthqueue = deque()
    sumqueue = deque()
    increases = 0
    for line in file:
        depth = int(line.strip("\r\n"))
        depthqueue.append(depth)
        if len(depthqueue) == 3:
            sumqueue.append(sum(depthqueue))
            if len(sumqueue) == 2:
                if sumqueue[0] < sumqueue[1]:
                    increases += 1
                sumqueue.popleft()
            depthqueue.popleft()
    return increases


# Begin options
use_example = False
mode = 2
# End options
puzzle_path = read_puzzle.make_puzzle_path(use_example, 1)
raw_puzzle = read_puzzle.get_puzzle_input(puzzle_path)
if mode == 1:
    print(part_one(raw_puzzle))
if mode == 2:
    print(part_two(raw_puzzle))
