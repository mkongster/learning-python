def max_subarray(numbers):
    """Find a contiguous subarray with the largest sum."""
    """Kadane's Algorithm"""
    best_sum = 0  # or: float('-inf')
    best_start = best_end = 0  # or: None
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            # Start a new sequence at the current element
            current_start = current_end
            current_sum = x
        else:
            # Extend the existing sequence with the current element
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1  # the +1 is to make 'best_end' exclusive

    return best_sum, best_start, best_end

def main():
    test_array = [5, 7, -3, 2, 9, 6, 16, 22, 21, 29, -14, 10, 5]
    best_sum, best_start, best_end = max_subarray(test_array)
    print('best_sum: {0}, best_start: {1}, best_end: {2}'.format(best_sum, best_start, best_end))

if __name__ == '__main__':
    main()