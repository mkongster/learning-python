

def pivot(index):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(a)
    a = a[-index:] + a[:-index]
    print(a)

def second_index_as_key(input):
    return input[1]

def main():
    test_list = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
    print(test_list)
    print(sorted(test_list))
    print(sorted(test_list, key=second_index_as_key))

if __name__ == "__main__":
    main()