from test_framework import generic_test


def reverse(x: int) -> int:
    sign = x > 0
    result = 0
    x = abs(x)
    while x:
        result *= 10
        result += x % 10
        x //= 10
    return result if sign else -result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
