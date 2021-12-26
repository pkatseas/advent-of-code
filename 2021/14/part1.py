from itertools import tee
from os import path
from typing import Counter

NUMBER_OF_STEPS = 10


def get_pairs(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as lines_input:
        lines = [line.strip() for line in lines_input.readlines()]

    template = lines[0]
    insertion_rules = {}
    for line in lines[2:]:
        element_pair, new_element = line.split(" -> ")
        insertion_rules[(element_pair[0], element_pair[1])] = new_element

    elements = list(template)

    for _ in range(NUMBER_OF_STEPS):
        new_elements = list(elements)
        for index, pair in enumerate(get_pairs(elements)):
            insertion_index = (index * 2) + 1
            insertion_element = insertion_rules[pair]
            new_elements.insert(insertion_index, insertion_element)

        elements = new_elements

    counts = Counter(elements).most_common()

    most_common_count = counts[0][1]
    least_common_count = counts[-1][1]

    print(f"Result is {most_common_count - least_common_count}")


if __name__ == "__main__":
    main()
