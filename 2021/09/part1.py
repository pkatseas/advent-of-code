from os import path
from typing import List, Optional


def get_adjacent_point(
    rows: List[str], row_index: int, column_index: int
) -> Optional[int]:
    try:
        return int(rows[row_index][column_index])
    except IndexError:
        return None


def get_adjacent_points(
    rows: List[str], row_index: int, column_index: int
) -> List[int]:
    adjacent_points = [
        get_adjacent_point(rows, row_index, column_index - 1),  # left
        get_adjacent_point(rows, row_index, column_index + 1),  # right
        get_adjacent_point(rows, row_index - 1, column_index),  # up
        get_adjacent_point(rows, row_index + 1, column_index),  # down
    ]

    # Clear out None values which indicate where there's no adjacent point
    return [point for point in adjacent_points if point is not None]


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as lines_input:
        rows = [line.strip() for line in lines_input.readlines()]

    low_points = []
    for row_index, row in enumerate(rows):
        for column_index, column in enumerate(row):
            adjacent_points = get_adjacent_points(rows, row_index, column_index)

            point = int(column)
            if all(point < adjacent_point for adjacent_point in adjacent_points):
                low_points.append(point)

    risk_level_total = sum(low_point + 1 for low_point in low_points)
    print(f"Low points: {low_points}\nSum of risk levels: {risk_level_total}")


if __name__ == "__main__":
    main()
