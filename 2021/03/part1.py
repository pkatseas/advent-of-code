from collections import Counter
from os import path


def main() -> None:
    base_dir = path.dirname(path.abspath(__file__))
    with open(path.join(base_dir, "input")) as instructions_input:
        measurements = instructions_input.read().splitlines()

    number_of_bits = len(measurements[0])

    bit_collectors = [[] for _ in range(number_of_bits)]
    for measurement in measurements:
        for index, bit in enumerate(measurement):
            bit_collectors[index].append(bit)

    most_common_bits = [
        Counter(bits).most_common(1)[0][0]  # returns [(bit, freq)]
        for bits in bit_collectors
    ]

    gamma_rate = "".join(most_common_bits)
    epsilon_rate = "".join("1" if bit == "0" else "0" for bit in gamma_rate)

    gamma_rate_int = int(gamma_rate, 2)
    epsilon_rate_int = int(epsilon_rate, 2)

    print(f"Gamma rate is: {gamma_rate} / {gamma_rate_int}")
    print(f"Epsilon rate is: {epsilon_rate} / {epsilon_rate_int}")
    print(f"Power consumption is: {gamma_rate_int * epsilon_rate_int}")


if __name__ == "__main__":
    main()
