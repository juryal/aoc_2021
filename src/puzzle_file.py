from pathlib import Path


def get_puzzle_input(path_string):
    puzzle_path = Path(path_string)
    if not puzzle_path.is_absolute():
        puzzle_path = Path(__file__).parent / puzzle_path
    with open(puzzle_path) as raw_puzzle_file:
        raw_puzzle = [line.strip() for line in raw_puzzle_file]
    return raw_puzzle
