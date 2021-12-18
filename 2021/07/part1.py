from os import path


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as crabs_input:
        crabs = [int(crab) for crab in crabs_input.read().split(",")]

    fuel = {}
    for position in range(min(crabs), max(crabs) + 1):
        fuel[position] = sum(abs(position - crab) for crab in crabs)

    min_fuel = None
    min_fuel_position = None
    for position, fuel in fuel.items():
        if min_fuel is None or fuel < min_fuel:
            min_fuel = fuel
            min_fuel_position = position

    print(
        f"The position requiring the least fuel is {min_fuel_position} with fuel {min_fuel}"
    )


if __name__ == "__main__":
    main()
