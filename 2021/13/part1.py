from os import path
from typing import NamedTuple, Set


class Dot(NamedTuple):
    x: int
    y: int


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

    first_fold = folds[0]
    fold_along, fold_position = first_fold.split("=")
    is_horizontal_fold = fold_along[-1] == "y"
    fold_position = int(fold_position)

    if is_horizontal_fold:
        new_dots = apply_horizontal_fold(dots, fold_position)
    else:
        new_dots = apply_vertical_fold(dots, fold_position)

    print(f"After the first fold, {len(new_dots)} dots are visible")


if __name__ == "__main__":
    main()
