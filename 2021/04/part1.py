from dataclasses import dataclass
from os import path
from typing import List


@dataclass
class BingoBoard:
    board: List[str]
    marked: List[str]

    _row_indices = [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24],
    ]
    _column_indices = [
        [0, 5, 10, 15, 20],
        [1, 6, 11, 16, 21],
        [2, 7, 12, 17, 22],
        [3, 8, 13, 18, 23],
        [4, 9, 14, 19, 24],
    ]

    def __init__(self):
        self.board = []
        self.marked = []

    def mark_number(self, number: str) -> None:
        self.marked.append(number)

    def wins(self) -> bool:
        for indices in [*self._column_indices, *self._row_indices]:
            if all(self.board[index] in self.marked for index in indices):
                return True

        return False

    def calculate_score(self) -> int:
        unmarked_numbers = [int(x) for x in self.board if x not in self.marked]
        last_called_number = int(self.marked[-1])
        return sum(unmarked_numbers) * last_called_number


def read_boards(lines: List[str]) -> List[BingoBoard]:
    boards = []

    current_board = BingoBoard()
    for line in lines[2:]:  # skipping past drawn numbers and first empty line
        if line == "":
            boards.append(current_board)
            current_board = BingoBoard()
            continue

        current_board.board.extend([x for x in line.strip().split(" ") if x != ""])

    # Append the last board too
    boards.append(current_board)

    return boards


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as bingo_input:
        lines = bingo_input.read().splitlines()

    drawn_numbers = lines[0]
    boards = read_boards(lines)

    for number in drawn_numbers.split(","):
        for board in boards:
            board.mark_number(number)

            if board.wins():
                print(f"Board {board} wins with score: {board.calculate_score()}")
                return


if __name__ == "__main__":
    main()
