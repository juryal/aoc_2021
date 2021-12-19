import read_puzzle


def naive_generation(generations: int, fish_list: list):
    for generation in range(generations):
        spawns = 0
        for fish in enumerate(fish_list):
            if fish[1] > 0:
                fish_list[fish[0]] -= 1
            elif fish[1] == 0:
                fish_list[fish[0]] = 6
                spawns += 1
            else:
                raise ValueError
        for spawn in range(spawns):
            fish_list.append(8)
    return len(fish_list)


def sort_fish(fish_list):
    fish_by_timer = {}
    for fish in fish_list:
        fish_by_timer[fish] = fish_by_timer.pop(fish, 0) + 1
    return fish_by_timer


def quicker_generation(generations, fish_list):
    fish_by_timer = sort_fish(fish_list)
    for generation in range(generations):
        new_fish_cohorts = {}
        for fish_cohort in fish_by_timer.items():
            if fish_cohort[0] == 0:
                new_fish_cohorts[8] = fish_cohort[1]
                new_fish_cohorts[6] = fish_cohort[1] + new_fish_cohorts.pop(6, 0)
                pass
            else:
                new_fish_cohorts[fish_cohort[0] - 1] = fish_cohort[
                    1
                ] + new_fish_cohorts.pop(fish_cohort[0] - 1, 0)
        fish_by_timer = new_fish_cohorts
    return sum(fish_by_timer.values())


# Begin options
use_example = False
generations = 256
# End options
puzzle_path = read_puzzle.make_puzzle_path(use_example, 6)
raw_puzzle = read_puzzle.get_puzzle_input(puzzle_path)
fish_list = [int(x) for x in raw_puzzle[0].split(",")]
print(quicker_generation(generations, fish_list))
