#!/usr/bin/python3
import sys


"""Represents a factorising fuction"""


def f_factorize_func(n):
    if n % 2 == 0:
        return 2, n // 2
    for f in range(3, int(n**0.5) + 1, 2):
        if n % f == 0:
            return f, n // f
    return n, 1


"""Represent the main entry for the function"""


def main():
    if len(sys.argv) != 2:
        print("Operation Failure")
        return

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            numbers = file.read().splitlines()

            for num in numbers:
                n = int(num)
                p, q = f_factorize_func(n)
                print(f"{n}={p}*{q}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except ValueError:
        print("Invalid number in the file.")


"""Represents the exectution of the function main"""


if __name__ == "__main__":
    main()
