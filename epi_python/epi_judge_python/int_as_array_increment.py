from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    length = len(A)
    index = -1
    carry = True
    while carry:
        # if index < -length:
        #     new = [1]
        #     new.extend(A)
        #     return new
        if index < -length:
            A[0] = 1
            A.append(0)
            return A
        if A[index] == 9:
            carry = True
            A[index] = 0
            index -= 1
        else:
            A[index] += 1
            return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
