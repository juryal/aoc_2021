import read_puzzle

# Begin options
use_example = True
# End options
puzzle_path = read_puzzle.make_puzzle_path(use_example, 8)
raw_puzzle = read_puzzle.get_puzzle_input(puzzle_path)
