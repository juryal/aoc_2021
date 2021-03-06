import read_puzzle


def oxygen_filter(report):
    if len(report) == 1:
        return report[0]
    ones_list = [x[1:] for x in report if int(x[0]) % 2]

    if len(ones_list) >= len(report) / 2:
        return "1" + oxygen_filter(ones_list)
    else:
        zeroes_list = [x[1:] for x in report if not int(x[0]) % 2]
        return "0" + oxygen_filter(zeroes_list)


def carbon_filter(report):
    if len(report) == 1:
        return report[0]
    zeroes_list = [x[1:] for x in report if not int(x[0]) % 2]

    if len(zeroes_list) <= len(report) / 2:
        return "0" + carbon_filter(zeroes_list)
    else:
        ones_list = [x[1:] for x in report if int(x[0]) % 2]
        return "1" + carbon_filter(ones_list)


def part_one(file):
    columntotals = [int(x) for x in file[0].strip("\r\n")]
    readings = 1
    for line in file:
        line = line.strip("\r\n")
        numbers = [int(x) for x in line]
        columntotals = [a + b for a, b in zip(numbers, columntotals)]
        readings += 1
    gamma = "0b" + "".join(
        [
            str(1) if columntotals[a] > (readings / 2) else str(0)
            for a in range(0, len(columntotals))
        ]
    )
    epsilon = "0b" + "".join(
        [
            str(1) if columntotals[a] < (readings / 2) else str(0)
            for a in range(0, len(columntotals))
        ]
    )
    return int(gamma, 2) * int(epsilon, 2)


def part_two(file):
    columntotals = [int(x) for x in file.readline().strip("\r\n")]
    readings = 1
    for line in file:
        line = line.strip("\r\n")
        numbers = [int(x) for x in line]
        columntotals = [a + b for a, b in zip(numbers, columntotals)]
        readings += 1


# Begin options
use_example = False
# End options
puzzle_path = read_puzzle.make_puzzle_path(use_example, 3)
raw_puzzle = read_puzzle.get_puzzle_input(puzzle_path)
print(part_one(raw_puzzle))
print(
    int("0b" + oxygen_filter(raw_puzzle), 2) * int("0b" + carbon_filter(raw_puzzle), 2)
)
