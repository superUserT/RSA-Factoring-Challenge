#!/usr/bin/python3
import sys

# Generate prime numbers on-the-fly using the Sieve of Eratosthenes
def primes_generator():
    primes = []
    num = 2
    while True:
        is_prime = all(num % prime != 0 for prime in primes)
        if is_prime:
            yield num
            primes.append(num)
        num += 1

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Improved factorization function using primes generator
def f_factorize_func(n, primes_gen):
    for f in primes_gen:
        if f * f > n:
            return n, 1
        if n % f == 0 and is_prime(n // f):
            return f, n // f
    return n, 1

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        return

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            numbers = file.read().splitlines()
            primes_gen = primes_generator()

            for num in numbers:
                n = int(num)
                p, q = f_factorize_func(n, primes_gen)
                print(f"{n} = {p} * {q}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except ValueError:
        print("Invalid number in the file.")

if __name__ == "__main__":
    main()
