#!/usr/bin/python3
import sys

# Improved prime checking function
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

# Generate prime numbers using the Sieve of Eratosthenes
def generate_primes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    return primes

# Improved factorization function using prime checking
def f_factorize_func(n, primes):
    for f in primes:
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
            max_num = max(map(int, numbers))
            primes = generate_primes(max_num)

            for num in numbers:
                n = int(num)
                p, q = f_factorize_func(n, primes)
                print(f"{n} = {p} * {q}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except ValueError:
        print("Invalid number in the file.")

if __name__ == "__main__":
    main()

