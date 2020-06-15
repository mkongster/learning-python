from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    lsb = x & ~(x - 1)
    pos = len(bin(lsb)) - 3
    if pos == 0:
        for index, value in enumerate(reversed(bin(x).split('0b')[1])):
            if value == '0':
                print(index)
                x ^= (1 << index) | (1 << (index - 1))
                return x
        length_bits = len(bin(x)) - 3
        x ^= (1 << length_bits) | (1 << (length_bits + 1))
        return x
    else:  
        x ^= (1 << pos) | (1 << (pos - 1))
        return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
