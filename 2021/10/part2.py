from os import path

CHARACTER_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as lines_input:
        rows = [line.strip() for line in lines_input.readlines()]

    open_to_close_character_map = {
        "[": "]",
        "{": "}",
        "(": ")",
        "<": ">",
    }

    open_characters = list(open_to_close_character_map.keys())

    row_scores = []
    for row in rows:
        row_score = 0

        opened = []
        for character in row:
            if character in open_characters:
                opened.append(character)
            else:
                last_open_character = opened.pop()
                expected_close_character = open_to_close_character_map[
                    last_open_character
                ]
                if character != expected_close_character:  # Corrupt line
                    opened = []  # this will exclude it from consideration below
                    break

        if not opened:
            continue

        for character in opened[::-1]:  # traverse from last to first
            missing_closing_character = open_to_close_character_map[character]
            row_score = (row_score * 5) + CHARACTER_SCORES[missing_closing_character]

        row_scores.append(row_score)

    sorted_scores = sorted(row_scores)
    middle_score = sorted_scores[int(len(sorted_scores) / 2)]

    print(f"Incomplete row scores {sorted_scores}\nMiddle score: {middle_score}")


if __name__ == "__main__":
    main()
