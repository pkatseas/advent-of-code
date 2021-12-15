from os import path


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as instructions_input:
        instructions = instructions_input.read().splitlines()

    position = 0
    depth = 0
    aim = 0

    for instruction in instructions:
        action, step = instruction.split(" ")
        step = int(step)

        if action == "forward":
            position += step
            depth += step * aim
        elif action == "down":
            aim += step
        elif action == "up":
            aim -= step

    print(f"Final position: {position}")
    print(f"Final depth: {depth}")
    print(f"Final aim: {aim}")
    print(f"Final calculation: {position * depth}")


if __name__ == "__main__":
    main()
