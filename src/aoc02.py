import read_puzzle


def part_one(file):
    horizontalposition = 0
    depth = 0
    for line in file:
        instruction = tuple(line.strip("\r\n").split())
        if instruction[0] == "forward":
            horizontalposition += int(instruction[1])
        elif instruction[0] == "down":
            depth += int(instruction[1])
        elif instruction[0] == "up":
            depth -= int(instruction[1])
    return horizontalposition * depth


def part_two(file):
    horizontalposition = 0
    depth = 0
    aim = 0
    for line in file:
        instruction = tuple(line.strip("\r\n").split())
        if instruction[0] == "forward":
            speed = int(instruction[1])
            horizontalposition += speed
            depth = depth + (aim * speed)
        elif instruction[0] == "down":
            aim += int(instruction[1])
        elif instruction[0] == "up":
            aim -= int(instruction[1])
    return horizontalposition * depth


# Begin options
use_example = False
mode = 2
# End options
puzzle_path = read_puzzle.make_puzzle_path(use_example, 2)
raw_puzzle = read_puzzle.get_puzzle_input(puzzle_path)
if mode == 1:
    print(part_one(raw_puzzle))
if mode == 2:
    print(part_two(raw_puzzle))
