from test_framework import generic_test

# O(n)
# def parity(x: int) -> int:
#     parity = 0
#     while x:
#         parity ^= x & 1
#         x >>= 1
#     return parity

# O(k), where k is the number of bits set to 1
# using x & (x - 1) equals x with the lowest bit erased
# def parity(x: int) -> int:
#     parity = 0
#     while x:
#         parity ^= 1
#         x &= x - 1
#     return parity

# O(log n)
# using XOR property, assuimg large 64-bit words
def parity(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
