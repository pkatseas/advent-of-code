from os import path


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as depth_input:
        depths = depth_input.read().splitlines()

    increasing_depths = 0
    previous_depth = None

    for depth_string in depths:
        depth = int(depth_string)

        if previous_depth is not None and depth > previous_depth:
            increasing_depths += 1

        previous_depth = depth

    print(f"Total number of increasing_depths: {increasing_depths}")


if __name__ == "__main__":
    main()
