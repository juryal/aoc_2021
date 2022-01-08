import read_puzzle


def is_unique(digit):
    unique_lengths = (2, 3, 4, 7)
    if len(digit) in unique_lengths:
        return True
    else:
        return False


def find_segments_ul_m(digits_to_segments):
    return digits_to_segments[4] - digits_to_segments[1]

def decipher_length_5_pattern(pattern, digits_to_segments):
    if set(pattern).issuperset(digits_to_segments[1]):
        return 3
    elif set(pattern).issuperset(digits_to_segments["ul_m"]):
        return 5
    else:
        return 2
def decipher_length_6_pattern(pattern, digits_to_segments):
    if set(pattern) == (digits_to_segments[8] - digits_to_segments["m"]):
        return 0
    elif set(pattern) == (digits_to_segments[5] | digits_to_segments["ll"]):
        return 6
    elif set(pattern) == (digits_to_segments[3] | digits_to_segments[4]):
        return 9
    else:
        raise Exception



def decipher_patterns(patterns):
    easy_patterns = filter(is_unique, patterns)
    easy_map = {2 : 1,3 :7, 4 : 4, 7 :8}
    segments_to_digits = dict()
    digits_to_segments = dict()
    for pattern in easy_patterns:
        segments_to_digits[pattern] = easy_map[len(pattern)]
        digits_to_segments[easy_map[len(pattern)]] = set(pattern)
    digits_to_segments["ul_m"] = find_segments_ul_m(digits_to_segments)
    length_5_patterns = list(filter(lambda x: len(x) == 5, patterns))
    for pattern in length_5_patterns:
        digit = decipher_length_5_pattern(pattern, digits_to_segments)
        digits_to_segments[digit] = set(pattern)
        segments_to_digits[pattern] = digit
    digits_to_segments["ll"] = digits_to_segments[2] - digits_to_segments[3]
    digits_to_segments["m"] = digits_to_segments["ul_m"] - (digits_to_segments[4] - digits_to_segments[3])
    length_6_patterns = list(filter(lambda x: len(x) == 6, patterns))
    for pattern in length_6_patterns:
        digit = decipher_length_6_pattern(pattern, digits_to_segments)
        segments_to_digits[pattern] = digit
    return segments_to_digits


def match_digit(digit, possible_keys):
    if len(possible_keys) == 0:
           return possible_keys[0]
    else:
        for key in possible_keys:
            if set(key) == set(digit):
                return key


def get_digits(map, digits):
    keys = list(map)
    raw_number = ""
    for digit in digits:
        possible_matches = list(filter(lambda x:len(x) == len(digit), keys))
        raw_number += str(map[match_digit(digit,possible_matches)])
    return int(raw_number)



def count_unique(line):
    output_digits = line.split("|")[-1].split()
    unique_digits = list(filter(is_unique, output_digits))
    return len(unique_digits)


def partone(raw_puzzle):
    return sum(count_unique(x) for x in raw_puzzle)

def parttwo(raw_puzzle):
    number = 0
    for line in raw_puzzle:
        line = line.split("|")
        map = decipher_patterns(line[0].split())
        number += get_digits(map,line[1].split())
    return number

# Begin options
use_example = False
# End options
puzzle_path = read_puzzle.make_puzzle_path(use_example, 8)
raw_puzzle = read_puzzle.get_puzzle_input(puzzle_path)
print(partone(raw_puzzle))
print(parttwo(raw_puzzle))