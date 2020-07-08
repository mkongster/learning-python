'''In the United States and Canada, phone numbers consist of ten digits, usually separated into a three-digit area code,
a three-digit exchange code, and a four digit station code.

Create a phone-number normalizer that takes any of the formats and returns a normalized number:
1-NNN-NNN-NNNN

Bonus: The first digit of the area code and the exchange code can only be 2-9,
and the second digit of an area code can't be 9. Use this information to validate the input.
'''

import re

def normalize_phone_numbers(number):
    pattern = r'(?P<country>[+1]+)?'r'[- (]?'r'(?P<area>[2-9][0-8]\d)'r'[-. )]+?'\
        r'(?P<exchange>\d{3})'r'[- .]'r'(?P<station>\d{4})'
    regex = re.compile(pattern)
    result = regex.search(number)
    if result:
        normal_number = '1-{area}-{exchange}-{station}'.format(area=result.group('area'),
            exchange=result.group('exchange'), station=result.group('station'))
    else:
        raise ValueError('invalid phone number: ' + number)
    return normal_number

def main():
    test_numbers = [
        '+1 223-456-7890',
        '1-223-456-7890',
        '+1 223 456-7890',
        '(223) 456-7890',
        '1 223 456 7890',
        '223.456.7890',
        '123 456 7890', #invalid
        '299 999 9999', #invalid
    ]

    for number in test_numbers:
        try:
            normal = normalize_phone_numbers(number)
            print(normal)
        except ValueError as e:
            print(e)
    

if __name__ == '__main__':
    main()