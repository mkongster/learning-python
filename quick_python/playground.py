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


def intToRoman(num: int) -> str:
    roman = ''
    
    roman_map = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }
    
    checker = 1000
    
    while checker:
        checker_count = num // checker
        print('checker_count: %s' % checker_count)
        if checker_count > 0:
            if checker_count == 9:
                roman += roman_map.get(checker)
                roman += roman_map.get(checker*10)
            elif checker_count == 4:
                roman += roman_map.get(checker)
                roman += roman_map.get(checker*5)
            if checker_count > 4 and checker_count < 9:
                roman += roman_map.get(checker*5)
                remainder = checker_count - 5
                print('remainder: %s' % remainder)
                if remainder > 0:
                    roman += roman_map.get(checker) * remainder
            if checker_count < 4:
                roman += roman_map.get(checker) * checker_count
            num %= checker

        checker //= 10
        print('checker: %s' % checker)
        print('num: %s' % num)
        
    return roman

def romanToInt(s: str) -> int:
    total = 0
    roman_map = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    holder = (s[0], roman_map[s[0]])
    
    for i in s:
        value = roman_map[i]
        print('value: %s' % value)
        print('holder: %s' % holder[1])
        if holder[1] < value:
            print(holder[0])
            total -= holder[1]
            print(total)
            value = roman_map.get(holder[0] + i)
        total += value
        holder = (i, roman_map[i])
    
    return total

def main():
    # test_array = [5, 7, -3, 2, 9, 6, 16, 22, 21, 29, -14, 10, 5]
    # best_sum, best_start, best_end = max_subarray(test_array)
    # print('best_sum: {0}, best_start: {1}, best_end: {2}'.format(best_sum, best_start, best_end))

    print(romanToInt('IV'))

if __name__ == '__main__':
    main()