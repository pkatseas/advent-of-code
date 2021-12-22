from functools import reduce
from os import path
from typing import List, NamedTuple, Optional


class Point(NamedTuple):
    number: int
    x: int
    y: int


def get_adjacent_point(
    rows: List[str], row_index: int, column_index: int
) -> Optional[Point]:
    if row_index >= 0 and column_index >= 0:
        try:
            return Point(
                number=int(rows[row_index][column_index]),
                x=row_index,
                y=column_index,
            )
        except IndexError:
            pass

    return None


def get_adjacent_points(
    rows: List[str], row_index: int, column_index: int
) -> List[Point]:
    adjacent_points = [
        get_adjacent_point(rows, row_index, column_index - 1),  # left
        get_adjacent_point(rows, row_index, column_index + 1),  # right
        get_adjacent_point(rows, row_index - 1, column_index),  # up
        get_adjacent_point(rows, row_index + 1, column_index),  # down
    ]

    # Clear out None values which indicate where there's no adjacent point
    return [point for point in adjacent_points if point is not None]


def get_basin_size(rows: List[str], low_point: Point) -> int:
    basin = [low_point]  # the total basin collection
    potential_basin_points = [low_point]  # the 'queue' of points to consider

    while potential_basin_points:
        point = potential_basin_points.pop()
        adjacent_points = get_adjacent_points(rows, point.x, point.y)

        new_points = [
            adjacent_point
            for adjacent_point in adjacent_points
            if adjacent_point.number < 9 and adjacent_point not in basin
        ]

        if new_points:
            basin.extend(new_points)
            potential_basin_points.extend(new_points)

    return len(basin)


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as lines_input:
        rows = [line.strip() for line in lines_input.readlines()]

    low_points = []
    for row_index, row in enumerate(rows):
        for column_index, column in enumerate(row):
            adjacent_points = get_adjacent_points(rows, row_index, column_index)

            point = int(column)
            if all(point < adjacent_point.number for adjacent_point in adjacent_points):
                low_points.append(Point(number=point, x=row_index, y=column_index))

    basin_sizes = [get_basin_size(rows, low_point) for low_point in low_points]

    top_three_basin_sizes = sorted(basin_sizes, reverse=True)[:3]
    top_three_basin_sizes_total = reduce(lambda x, y: x * y, top_three_basin_sizes)

    print(
        f"Top three largest basin sizes: {top_three_basin_sizes}"
        f"\nTotal: {top_three_basin_sizes_total}"
    )


if __name__ == "__main__":
    main()
