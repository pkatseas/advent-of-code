from os import path
from typing import NamedTuple, Set


class Dot(NamedTuple):
    x: int
    y: int

    def __lt__(self, dot) -> bool:
        return self.y < dot.y or (self.y == dot.y and self.x < dot.x)


def apply_horizontal_fold(dots: Set[Dot], fold_position: int):
    new_dots = set()

    for dot in dots:
        if dot.y > fold_position:
            new_dots.add(Dot(x=dot.x, y=((fold_position * 2) - dot.y)))
        else:
            new_dots.add(dot)

    return new_dots


def apply_vertical_fold(dots: Set[Dot], fold_position: int) -> Set[Dot]:
    new_dots = set()

    for dot in dots:
        if dot.x > fold_position:
            new_dots.add(Dot(y=dot.y, x=((fold_position * 2) - dot.x)))
        else:
            new_dots.add(dot)

    return new_dots


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as lines_input:
        lines = [line.strip() for line in lines_input.readlines()]

    dots = set()
    folds = []
    for line in lines:
        if "," in line:
            x, y = line.split(",")
            dots.add(Dot(x=int(x), y=int(y)))
        elif "fold along" in line:
            folds.append(line)

    for fold in folds:
        fold_along, fold_position = fold.split("=")
        is_horizontal_fold = fold_along[-1] == "y"
        fold_position = int(fold_position)

        if is_horizontal_fold:
            dots = apply_horizontal_fold(dots, fold_position)
        else:
            dots = apply_vertical_fold(dots, fold_position)

    number_of_rows = 0
    number_of_columns = 0

    for dot in dots:
        number_of_rows = max(number_of_rows, dot.y)
        number_of_columns = max(number_of_columns, dot.x)

    rows = [
        [" " for _ in range(number_of_columns + 1)] for _ in range(number_of_rows + 1)
    ]
    for dot in dots:
        rows[dot.y][dot.x] = "#"

    for row in rows:
        print("".join(row))


if __name__ == "__main__":
    main()
