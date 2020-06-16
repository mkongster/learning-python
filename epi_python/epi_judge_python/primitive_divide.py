from test_framework import generic_test

# do as much work as possible with each iteration
def divide(x: int, y: int) -> int:
    quotient = 0
    power = 32 # max bits
    y_power = y << power
    while x >= y:
        # find the largest k, such that (2**k)y <= x
        while y_power > x:
            y_power >>= 1
            power -= 1
        
        # add k to the quotient
        quotient += 1 << power
        x -= y_power
    return quotient


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
