from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return y
    if y == 1:
        return x

    def add(a, b):
        while b:
            carry = a & b
            a, b = a ^ b, carry << 1
        return a
    total_sum = 0

    while x:
        if x & 1:
            total_sum = add(total_sum, y)
        x, y = x >> 1, y << 1
    return total_sum



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
