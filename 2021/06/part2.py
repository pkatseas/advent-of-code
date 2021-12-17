from os import path
from typing import Dict

NUMBER_OF_DAYS = 256


def initialise_counts_per_timer() -> Dict[int, int]:
    return {i: 0 for i in range(9)}


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as lanternfish_input:
        initial_lanternfish = lanternfish_input.read()

    fish_count_per_timer = initialise_counts_per_timer()

    for fish in initial_lanternfish.split(","):
        fish_count_per_timer[int(fish)] += 1

    for _ in range(NUMBER_OF_DAYS):
        new_fish_count_per_timer = initialise_counts_per_timer()
        for timer, fish_count in fish_count_per_timer.items():
            if timer == 0:
                new_fish_count_per_timer[6] += fish_count
                new_fish_count_per_timer[8] += fish_count
            else:
                new_fish_count_per_timer[timer - 1] += fish_count

        fish_count_per_timer = new_fish_count_per_timer

    print(
        f"After {NUMBER_OF_DAYS} days, we have {sum(fish_count_per_timer.values())} lanternfish"
    )


if __name__ == "__main__":
    main()
