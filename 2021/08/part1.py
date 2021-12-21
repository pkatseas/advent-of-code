from os import path


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as lines_input:
        lines = lines_input.readlines()

    number_of_easy_digits = 0
    for line in lines:
        _line_signal_patterns, line_output_values = line.strip().split(" | ")
        for token in line_output_values.split(" "):
            if len(token) in (
                2,  # represents 1
                3,  # represents 7
                4,  # represents 4
                7,  # represents 8
            ):
                number_of_easy_digits += 1

    print(f"{number_of_easy_digits} easy digits (1, 4, 7, 8) were found.")


if __name__ == "__main__":
    main()
