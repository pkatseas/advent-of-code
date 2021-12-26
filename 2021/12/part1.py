from collections import defaultdict
from os import path

START_NODE = "start"
END_NODE = "end"


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
                if not (
                    # big caves can always be added, no matter how many times
                    potential_next_cave.isupper()
                    # small caves can only be added once, so don't re-add when present
                    or potential_next_cave not in path_to_process
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
