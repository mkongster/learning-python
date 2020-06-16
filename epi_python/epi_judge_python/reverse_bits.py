from test_framework import generic_test
from swap_bits import swap_bits

# brute force
def reverse_bits(x: int) -> int:
    msb = len(bin(x)) - 3
    i = 0
    while msb > i:
        x = swap_bits(x, i, msb)
        i += 1
        msb -= 1
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
