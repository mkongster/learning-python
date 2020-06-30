from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    furthest = 0
    index, length = 0, len(A)
    while furthest < length and index <= furthest:
        furthest = max(A[index] + index, furthest)
        index += 1
    return furthest >= (length - 1)
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
