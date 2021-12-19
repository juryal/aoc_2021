import read_puzzle
import statistics


def triangle_number(n: int):
    return int(((n ** 2) + n) / 2)


def search_positions_one(position: int, positions: list, increment: int, previous=None):
    moves = sum([abs(x - position) for x in positions])
    if previous is None or moves <= previous:
        return search_positions_one(position + increment, positions, increment, moves)
    elif moves > previous:
        return previous
    else:
        raise Exception


def search_positions_two(position: int, positions: list, increment: int, previous=None):
    moves = sum([triangle_number(abs(x - position)) for x in positions])
    if previous is None or moves <= previous:
        return search_positions_two(position + increment, positions, increment, moves)
    elif moves > previous:
        return previous
    else:
        raise Exception


def part_one(raw_puzzle):
    positions = [int(x) for x in raw_puzzle[0].split(",")]
    median_position = statistics.median_high(positions)
    moves = search_positions_one(median_position, positions, 1)
    return min(moves, search_positions_one(median_position, positions, -1, moves))


def part_two(raw_puzzle):
    positions = [int(x) for x in raw_puzzle[0].split(",")]
    median_position = statistics.median_high(positions)
    moves = search_positions_two(median_position, positions, 1)
    return min(moves, search_positions_two(median_position, positions, -1, moves))


# Begin options
use_example = False
# End options
puzzle_path = read_puzzle.make_puzzle_path(use_example, 7)
raw_puzzle = read_puzzle.get_puzzle_input(puzzle_path)
print(part_one(raw_puzzle))
print(part_two(raw_puzzle))
