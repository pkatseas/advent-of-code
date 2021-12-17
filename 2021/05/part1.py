from collections import Counter
from dataclasses import dataclass
from os import path
from typing import List, Tuple


@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def is_vertical(self):
        return self.x1 == self.x2

    def is_horizontal(self):
        return self.y1 == self.y2


def parse_lines(lines_data: List[str]) -> List[Line]:
    lines = []
    for line_data in lines_data:
        start_coordinates, end_coordinates = line_data.split(" -> ")
        x1, y1 = start_coordinates.split(",")
        x2, y2 = end_coordinates.split(",")

        lines.append(Line(x1=int(x1), y1=int(y1), x2=int(x2), y2=int(y2)))

    return lines


def filter_lines(lines: List[Line]) -> List[Line]:
    # Filter by horizontal and vertical lines only
    return [line for line in lines if line.is_vertical() or line.is_horizontal()]


def get_line_points(line: Line) -> List[Tuple[int, int]]:
    points = []

    if line.is_horizontal():
        for index in range(min(line.x1, line.x2), max(line.x1, line.x2) + 1):
            points.append((index, line.y1))
    if line.is_vertical():
        for index in range(min(line.y1, line.y2), max(line.y1, line.y2) + 1):
            points.append((line.x1, index))

    return points


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as lines_input:
        lines_data = lines_input.read().splitlines()

    lines = parse_lines(lines_data)
    lines = filter_lines(lines)

    points = []
    for line in lines:
        points.extend(get_line_points(line))

    point_occurences = Counter(points)

    dangerous_points = [
        point for point, occurences in point_occurences.items() if occurences > 1
    ]
    print(
        f"{len(dangerous_points)} points have at least 2 overlapping lines over them:"
        f"\n{dangerous_points}"
    )


if __name__ == "__main__":
    main()
