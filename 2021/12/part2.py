from collections import Counter, defaultdict
from os import path
from typing import List

START_NODE = "start"
END_NODE = "end"


def can_cave_be_added(path: List[str], cave: str) -> bool:
    # Big caves can always be added, no matter how many times
    if cave.isupper():
        return True

    # Small caves which are not part of the path already can just be added
    if cave not in path:
        return True

    # Otherwise, we have a small cave that's already part of the path. In this case we
    # can only re-add it to the path if no small cave was already seen twice.
    return not any(
        cave.islower() and count == 2 for cave, count in Counter(path).items()
    )


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as lines_input:
        lines = [line.strip() for line in lines_input.readlines()]

    cave_map = defaultdict(list)
    for line in lines:
        cave1, cave2 = line.split("-")
        cave_map[cave1].append(cave2)
        cave_map[cave2].append(cave1)

    distinct_paths = []
    paths_to_process = [
        [START_NODE],
    ]
    while paths_to_process:
        new_paths_to_process = []

        for path_to_process in paths_to_process:
            last_cave = path_to_process[-1]
            potential_next_caves = cave_map[last_cave]

            for potential_next_cave in potential_next_caves:
                if potential_next_cave == START_NODE or not can_cave_be_added(
                    path_to_process, potential_next_cave
                ):
                    continue

                new_path = [*path_to_process, potential_next_cave]

                if potential_next_cave == END_NODE:
                    distinct_paths.append(new_path)
                else:
                    new_paths_to_process.append(new_path)

        paths_to_process = new_paths_to_process

    print(f"There's a total of {len(distinct_paths)} distinct paths")


if __name__ == "__main__":
    main()
