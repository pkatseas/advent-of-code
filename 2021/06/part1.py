from dataclasses import dataclass
from os import path

NUMBER_OF_DAYS = 80


@dataclass
class Lanternfish:
    timer: int

    def __init__(self, timer: int = 8) -> None:
        self.timer = timer

    def tick(self) -> bool:
        """
        Ticks a day for the lanternfish. If it's at the point of producing anoter
        lanternfish, it returns True.
        """
        if self.timer == 0:
            self.timer = 6
            return True

        self.timer -= 1
        return False


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as lanternfish_input:
        initial_lanternfish = lanternfish_input.read()

    lanternfish = [Lanternfish(int(timer)) for timer in initial_lanternfish.split(",")]

    for _ in range(NUMBER_OF_DAYS):
        new_fish = []
        for fish in lanternfish:
            if fish.tick():
                new_fish.append(Lanternfish())
        lanternfish.extend(new_fish)

    print(f"After {NUMBER_OF_DAYS} days, we have {len(lanternfish)} lanternfish")


if __name__ == "__main__":
    main()
