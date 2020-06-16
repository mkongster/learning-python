from test_framework import generic_test

import math

def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    if x == 0:
        return True
    digits = math.floor(math.log10(x)) + 1
    while digits > 0:
        if digits == 1:
            return True

        msd = x // (10 ** (digits - 1))
        lsd = x % 10
        
        if msd != lsd:
            return False
        x %= 10 ** (digits - 1)
        digits -= 2
        x //= 10
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
