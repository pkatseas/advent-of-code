from collections import defaultdict
from os import path
from typing import Dict


def get_digit_map_from_signal_patterns(signal_patterns: str) -> Dict[str, str]:
    signal_pattern_to_digit_map = {}
    digit_to_signal_pattern_map = {}

    signal_pattern_length_to_signal_pattern_map = defaultdict(list)

    for signal_pattern in signal_patterns.split(" "):
        signal_pattern_length_to_signal_pattern_map[len(signal_pattern)].append(
            signal_pattern
        )

    # Easy digits: there's only one signal pattern with the given length
    for digit, digit_signal_pattern_length in {"1": 2, "7": 3, "4": 4, "8": 7}.items():
        signal_pattern = signal_pattern_length_to_signal_pattern_map[
            digit_signal_pattern_length
        ][0]
        signal_pattern_to_digit_map[signal_pattern] = digit
        digit_to_signal_pattern_map[digit] = signal_pattern

    # Harder digits: there's 3 signal patterns per length 5 or 6
    signal_patterns_for_length_5 = signal_pattern_length_to_signal_pattern_map[5]
    signal_patterns_for_length_6 = signal_pattern_length_to_signal_pattern_map[6]

    digit_7_signal_pattern = digit_to_signal_pattern_map["7"]

    # Digit 3: the only digit with length 5 that has all characters in digit 7
    for signal_pattern in signal_patterns_for_length_5:
        if all(char in signal_pattern for char in digit_7_signal_pattern):
            digit = "3"
            signal_pattern_to_digit_map[signal_pattern] = digit
            digit_to_signal_pattern_map[digit] = signal_pattern

    digit_3_signal_pattern = digit_to_signal_pattern_map["3"]

    # Digit 9: the only digit with length 6 that has all characters in digit 3
    for signal_pattern in signal_patterns_for_length_6:
        if all(char in signal_pattern for char in digit_3_signal_pattern):
            digit = "9"
            signal_pattern_to_digit_map[signal_pattern] = digit
            digit_to_signal_pattern_map[digit] = signal_pattern

    # Digit 6: the only digit with length 6 that doesn't have all characters in digit 7
    for signal_pattern in signal_patterns_for_length_6:
        if not all(char in signal_pattern for char in digit_7_signal_pattern):
            digit = "6"
            signal_pattern_to_digit_map[signal_pattern] = digit
            digit_to_signal_pattern_map[digit] = signal_pattern

    digit_6_signal_pattern = digit_to_signal_pattern_map["6"]
    digit_9_signal_pattern = digit_to_signal_pattern_map["9"]

    # Digit 0: the only digit with length 6 still unknown
    for signal_pattern in signal_patterns_for_length_6:
        if signal_pattern not in (digit_9_signal_pattern, digit_6_signal_pattern):
            digit = "0"
            signal_pattern_to_digit_map[signal_pattern] = digit
            digit_to_signal_pattern_map[digit] = signal_pattern

    # Digit 5: the only digit with length 5 whose characters are all in digit 6's characters
    for signal_pattern in signal_patterns_for_length_5:
        if all(char in digit_6_signal_pattern for char in signal_pattern):
            digit = "5"
            signal_pattern_to_digit_map[signal_pattern] = digit
            digit_to_signal_pattern_map[digit] = signal_pattern

    digit_5_signal_pattern = digit_to_signal_pattern_map["5"]

    # Digit 2: the only digit with length 5 still unknown
    for signal_pattern in signal_patterns_for_length_5:
        if signal_pattern not in (digit_5_signal_pattern, digit_3_signal_pattern):
            digit = "2"
            signal_pattern_to_digit_map[signal_pattern] = digit
            digit_to_signal_pattern_map[digit] = signal_pattern

    return signal_pattern_to_digit_map


def get_output_value_from_line_output_value_signal_patterns(
    signal_pattern_to_digit_map: Dict[str, str], line_output_value_signal_patterns: str
) -> int:
    output_value = ""
    for output_value_signal_pattern in line_output_value_signal_patterns.split(" "):
        output_value_signal_pattern_length = len(output_value_signal_pattern)
        for signal_pattern, digit in signal_pattern_to_digit_map.items():
            if output_value_signal_pattern_length == len(signal_pattern) and all(
                char in signal_pattern for char in output_value_signal_pattern
            ):
                output_value += digit
                break

    return int(output_value)


def get_output_value_from_line(line: str) -> int:
    line_signal_patterns, line_output_value_signal_patterns = line.strip().split(" | ")
    signal_pattern_to_digit_map = get_digit_map_from_signal_patterns(
        line_signal_patterns
    )
    return get_output_value_from_line_output_value_signal_patterns(
        signal_pattern_to_digit_map, line_output_value_signal_patterns
    )


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as lines_input:
        lines = lines_input.readlines()

    output_values = [get_output_value_from_line(line) for line in lines]

    print(
        f"Output values: {output_values}\nSum of all output values: {sum(output_values)}"
    )


if __name__ == "__main__":
    main()
