from itertools import tee
from math import ceil
from os import path
from typing import Counter

NUMBER_OF_STEPS = 40


def get_pairs(iterable):
    a, b = tee(iterable)
    next(b, None)
    return list(zip(a, b))


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as lines_input:
        lines = [line.strip() for line in lines_input.readlines()]

    template = lines[0]
    insertion_rules = {}
    for line in lines[2:]:
        element_pair, new_element = line.split(" -> ")
        insertion_rules[(element_pair[0], element_pair[1])] = new_element

    pairs = get_pairs(template)

    pair_counts = Counter(pairs)  # initialise the pair counts

    for _ in range(NUMBER_OF_STEPS):
        new_pair_counts = Counter()
        for pair, count in pair_counts.items():
            insertion_element = insertion_rules[pair]

            # Generate new pairs and attach the current count
            new_pair_counts[(pair[0], insertion_element)] += count
            new_pair_counts[(insertion_element, pair[1])] += count

        pair_counts = new_pair_counts

    element_counts = Counter()
    for pair, count in pair_counts.items():
        # Add counts for both elements in the pair
        element_counts[pair[0]] += count
        element_counts[pair[1]] += count

    counts = element_counts.most_common()

    # Get actual element count -- at this point we've double-counted the elements due to
    # each element appearing in 2 pairs.
    most_common_count = ceil(counts[0][1] / 2)
    least_common_count = ceil(counts[-1][1] / 2)

    print(f"Result is {most_common_count - least_common_count}")


if __name__ == "__main__":
    main()
