import puzzle_file


def naive_generation(generations, fish_list):
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


run_on_example = False
puzzle_path = "../puzzles/day06"
if run_on_example:
    puzzle_path = puzzle_path + "_example"
puzzle_path = puzzle_path + ".txt"
generations = 256
raw_puzzle = puzzle_file.get_puzzle_input(puzzle_path)
fish_list = [int(x) for x in raw_puzzle[0].split(",")]
print(quicker_generation(generations, fish_list))
