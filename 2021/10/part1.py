from os import path


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

    incorrect_close_characters = []
    for row in rows:
        opened = []
        for character in row:
            if character in open_characters:
                opened.append(character)
            else:
                last_open_character = opened.pop()
                expected_close_character = open_to_close_character_map[
                    last_open_character
                ]
                if character != expected_close_character:
                    incorrect_close_characters.append(character)
                    break

    character_scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    total_score = sum(
        [character_scores[character] for character in incorrect_close_characters]
    )

    print(
        f"Found incorrect closing characters {incorrect_close_characters}"
        f"\nTotal score: {total_score}"
    )


if __name__ == "__main__":
    main()
