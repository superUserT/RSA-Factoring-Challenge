#!/usr/bin/python3
import sys


"""Represents a prime checking fuction"""
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


"""Represents a factorising fuction"""
def factorize_rsa(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return i, n // i
    return n, 1


"""Represent the main entry for the function"""
def main():
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        return

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            rsa_number = int(file.read().strip())
            p, q = factorize_rsa(rsa_number)
            print(f"{rsa_number}={p}*{q}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except ValueError:
        print("Invalid number in the file.")


"""Represents the exectution of the function main"""
if __name__ == "__main__":
    main()

