from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.

# def generate_primes(n: int) -> List[int]:
#     primes = []
#     for i in range(2, n + 1):
#         count = 0
#         for j in range(2, i + 1):
#             if i % j == 0:
#                 count += 1
#         if count == 1:
#             primes.append(i)
#     return primes

# def generate_primes(n: int) -> List[int]:
#     primes = []
#     # is_prime[p] represents if p is prime or not. 
#     # Initially set each to True, expecting 0 and 1, then use sieving to eliminate nonprimes.
#     is_prime = [False, False] + [True] * (n - 1)
#     for i in range(2, n + 1):
#         if is_prime[i]:
#             primes.append(i)
#             for i in range(i * 2, n + 1, i):
#                 is_prime[i] = False
#     return primes


def generate_primes(n: int) -> List[int]:
    if n < 2:
        return []
    size = (n - 3) // 2 + 1
    primes = [2]
    # is_prime[i] reprsents (2i + 3) is prime or not.
    # For example, is_prime[0] represents 3 is prime or not, is_prime[1] represents 5, is_prime[2] represents 7, etc
    # Initially set each to true, Then use sieving to eliminate nonprimes.
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            # Sieving from p^2, where p^2 = (4i^2 + 12i + 9).
            # The index in is_prime is (2i62 + 6i + 3) because is_prime[i] represents 2i + 3.
            # Note that we need to use long for j because p^2 mightr overflow.
            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
