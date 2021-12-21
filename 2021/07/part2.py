from os import path


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as crabs_input:
        crabs = [int(crab) for crab in crabs_input.read().split(",")]

    min_fuel = None
    min_fuel_position = None
    for position in range(min(crabs), max(crabs) + 1):
        fuel_for_position = sum(
            sum(range(1, abs(position - crab) + 1)) for crab in crabs
        )
        if min_fuel is None or fuel_for_position < min_fuel:
            min_fuel = fuel_for_position
            min_fuel_position = position

    print(
        f"The position requiring the least fuel is {min_fuel_position} with fuel {min_fuel}"
    )


if __name__ == "__main__":
    main()
