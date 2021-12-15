from os import path


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as depth_input:
        depths = depth_input.read().splitlines()

    depths = [int(depth) for depth in depths]

    slice_start = 0
    slice_end = 3

    depth_sums = []
    while slice_end <= len(depths):
        depth_sums.append(sum(depths[slice_start:slice_end]))

        slice_start += 1
        slice_end += 1

    previous_depth_sum = None
    increasing_depth_sums = 0

    for depth_sum in depth_sums:
        if previous_depth_sum is not None and depth_sum > previous_depth_sum:
            increasing_depth_sums += 1

        previous_depth_sum = depth_sum

    print(f"Total number of increasing depth sums: {increasing_depth_sums}")


if __name__ == "__main__":
    main()
