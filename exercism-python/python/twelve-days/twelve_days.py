def recite(start_verse, end_verse):
    gift_map = {
        1: ('first', 'a Partridge in a Pear Tree'),
        2: ('second', 'two Turtle Doves'),
        3: ('third', 'three French Hens'),
        4: ('fourth', 'four Calling Birds'),
        5: ('fifth', 'five Gold Rings'),
        6: ('sixth', 'six Geese-a-Laying'),
        7: ('seventh', 'seven Swans-a-Swimming'),
        8: ('eighth', 'eight Maids-a-Milking'),
        9: ('ninth', 'nine Ladies Dancing'),
        10: ('tenth', 'ten Lords-a-Leaping'),
        11: ('eleventh', 'eleven Pipers Piping'),
        12: ('twelfth', 'twelve Drummers Drumming')
    }

    beginning = 'On the {day} day of Christmas my true love gave to me: {gifts}.'
    verse = []
    for i in range(start_verse, end_verse + 1):
        gifts = []
        for j in reversed(range(i)):
            if j == 0 and gifts:
                gift = 'and ' + gift_map[j+1][1]
            else:
                gift = gift_map[j+1][1]
            gifts.append(gift)
        gift_data = gift_map[i]
        gifts_string = ', '.join(gifts)
        line = beginning.format(day=gift_data[0], gifts=gifts_string)
        verse.append(line)
    return verse


def main():
    expected = [recite(n, n)[0] for n in range(1, 4)]
    print(expected)
    print(recite(1,3))
    print(recite(2,2))


if __name__ == "__main__":
    main()
