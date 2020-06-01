def distance(strand_a, strand_b):
    len_a = len(strand_a)
    len_b = len(strand_b)

    if len_a != len_b:
        raise ValueError('You dun goofed')

    if len_a == 1 and len_b == 1:
        if strand_a != strand_b:
            return 1
        else:
            return 0
    if strand_a != strand_b:
        top =  distance(strand_a[:int(len_a/2)], strand_b[:int(len_b/2)])
        bottom = distance(strand_a[int(len_a/2):], strand_b[int(len_b/2):])
        return top + bottom
    else:
        return 0