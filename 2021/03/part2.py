from collections import Counter
from os import path
from typing import List

ZERO = "0"
ONE = "1"


def find_rating(measurements: List[str], most_common: bool = True) -> str:
    potential_measurements = measurements

    bit_index = 0
    while bit_index < len(measurements[0]):
        new_potential_measurements = []

        counter = Counter(
            [measurement[bit_index] for measurement in potential_measurements]
        )
        counter_of_0 = counter[ZERO]
        counter_of_1 = counter[ONE]

        if most_common:
            bit_criterion = ONE if counter_of_1 >= counter_of_0 else ZERO
        else:
            bit_criterion = ZERO if counter_of_0 <= counter_of_1 else ONE

        for measurement in potential_measurements:
            if measurement[bit_index] == bit_criterion:
                new_potential_measurements.append(measurement)

        potential_measurements = new_potential_measurements

        if len(potential_measurements) == 1:
            return potential_measurements[0]

        bit_index += 1

    raise ValueError("Couldn't find rating!")


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as instructions_input:
        measurements = instructions_input.read().splitlines()

    oxygen_generator_rating = find_rating(measurements)
    co2_scrubber_rating = find_rating(measurements, most_common=False)

    oxygen_generator_rating_int = int(oxygen_generator_rating, 2)
    co2_scrubber_rating_int = int(co2_scrubber_rating, 2)

    print(
        f"Oxygen generator rating is: {oxygen_generator_rating} / {oxygen_generator_rating_int}"
    )
    print(f"CO2 scrubber rating is: {co2_scrubber_rating} / {co2_scrubber_rating_int}")
    print(
        f"Life support rating is: {co2_scrubber_rating_int * oxygen_generator_rating_int}"
    )


if __name__ == "__main__":
    main()
