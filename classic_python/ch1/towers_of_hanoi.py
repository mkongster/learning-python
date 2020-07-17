# def hanoi(begin, end, temp, n):
#     if n == 1:
#         end.push(begin.pop())
#     else:
#         hanoi(begin, temp, end, n - 1)
#         hanoi(begin, end, temp, 1)
#         hanoi(temp, end, begin, n - 1)

def hanois(towers, n):
    print(towers)
    if n == 1:
        towers[1].append(towers[0].pop())
    else:
        hanois([towers[0]] + towers[2:] + [towers[1]], n - 1)
        hanois([towers[0]] + [towers[1]] + towers[2:], 1)
        hanois(towers[2:] + [towers[1]] + [towers[0]], n - 1)


def main():
    num_discs = 3
    tower_a = []
    tower_b = []
    tower_c = []
    tower_d = []

    for i in range(1, num_discs + 1):
        tower_a.append(i)

    towers = [tower_a, tower_d, tower_b, tower_c]
    hanois(towers, 3)
    print(tower_a)
    print(tower_b)
    print(tower_c)
    print(tower_d)


if __name__ == "__main__":
    main()
