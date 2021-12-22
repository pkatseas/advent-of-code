from os import path
from typing import List


def increase_octopus_energy_level(octopuses: List[List[int]], x: int, y: int) -> None:
    if x < 0 or y < 0:  # skip negative indexing so we don't wrap around the ends
        return

    try:
        octopuses[x][y] += 1
    except IndexError:
        return  # tried to access out of bounds index, nothing to do as it doesn't exist

    if octopuses[x][y] == 10:
        for adjacent_x, adjacent_y in (
            (x + 1, y),  # right
            (x - 1, y),  # left
            (x, y + 1),  # bottom
            (x, y - 1),  # top
            (x - 1, y - 1),  # diagonal top left
            (x + 1, y - 1),  # diagonal top right
            (x - 1, y + 1),  # diagonal bottom left
            (x + 1, y + 1),  # diagonal bottom right
        ):
            increase_octopus_energy_level(octopuses, adjacent_x, adjacent_y)


def did_all_octopuses_flash(octopuses: List[List[int]]) -> bool:
    flashes = 0

    for x, row in enumerate(octopuses):
        for y, octopus in enumerate(row):
            increase_octopus_energy_level(octopuses, x, y)

    for x, row in enumerate(octopuses):
        for y, octopus in enumerate(row):
            if octopus > 9:
                flashes += 1  # count the flash
                octopuses[x][y] = 0  # reset the energy level

    return flashes == len(octopuses) * len(octopuses[0])  # Should be 100


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as lines_input:
        lines = [line.strip() for line in lines_input.readlines()]

    octopuses = [[int(octopus) for octopus in line] for line in lines]

    step = 1
    while True:
        if did_all_octopuses_flash(octopuses):
            print(f"All octopuses synced their flash for the first time on step {step}")
            return

        step += 1


if __name__ == "__main__":
    main()
