import read_puzzle


def is_unique(digit):
    unique_lengths = (2, 3, 4, 7)
    if len(digit) in unique_lengths:
        return True
    else:
        return False


def count_unique(line):
    output_digits = line.split("|")[-1].split()
    unique_digits = list(filter(is_unique, output_digits))
    return len(unique_digits)


def partone(raw_puzzle):
    # Sum of occurences of 1, 4, 7, or 8 in each line
    return sum(count_unique(x) for x in raw_puzzle)


# Begin options
use_example = False
# End options
puzzle_path = read_puzzle.make_puzzle_path(use_example, 8)
raw_puzzle = read_puzzle.get_puzzle_input(puzzle_path)
print(partone(raw_puzzle))
