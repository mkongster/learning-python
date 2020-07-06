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



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
