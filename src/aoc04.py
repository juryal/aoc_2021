import read_puzzle
import copy


def part_one(bingo_boards, raw_called_numbers):
    bingo_boards = copy.deepcopy(bingo_boards)
    for draw in raw_called_numbers:
        for board in bingo_boards:
            for line in enumerate(board):
                for square in enumerate(line[1]):
                    if square[1] == draw:
                        board[line[0]][square[0]] = None
                        row = {
                            board[line[0]][x] if board[line[0]][x] else 0
                            for x in range(0, 5)
                        }
                        column = {
                            board[x][square[0]] if board[x][square[0]] else 0
                            for x in range(0, 5)
                        }
                        pass
                        if len(row) == 1 or len(column) == 1:
                            return (
                                sum(sum(y if y else 0 for y in x) for x in board) * draw
                            )


def part_two(bingo_boards, raw_called_numbers):
    for draw in raw_called_numbers:
        starting_boards = enumerate(bingo_boards)
        removal_list = []
        for enumerated_board in starting_boards:
            board = enumerated_board[1]
            for line in enumerate(board):
                for square in enumerate(line[1]):
                    if square[1] == draw:
                        board[line[0]][square[0]] = None
                        row = {board[line[0]][x] for x in range(0, 5)}
                        column = {board[x][square[0]] for x in range(0, 5)}
                        pass
                        if len(row) == 1 or len(column) == 1:
                            last_winner = board
                            last_draw = draw
                            removal_list.append(enumerated_board[0])
        for index in sorted(removal_list, reverse=True):
            del bingo_boards[index]
    return sum(sum(y if y else 0 for y in x) for x in last_winner) * last_draw


# Begin options
use_example = False
# End options
puzzle_path = read_puzzle.make_puzzle_path(use_example, 4)
raw_puzzle = read_puzzle.get_puzzle_input(puzzle_path)
raw_called_numbers = [int(x) for x in raw_puzzle.pop(0).split(",")]
bingo_boards = []
bingo_board = []
for line in raw_puzzle:
    line = line
    if not line and bingo_board:
        bingo_boards.append(bingo_board)
        bingo_board = []
    elif line:
        bingo_board.append([int(x) for x in line.split()])
bingo_boards.append(bingo_board)

print(part_one(bingo_boards, raw_called_numbers))
print(part_two(bingo_boards, raw_called_numbers))
