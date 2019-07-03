from set import *


def main():
    set1 = make_set(1)
    set2 = make_set(2)
    set3 = make_set(3)
    print(find_set(set1))
    print(find_set(set2))
    print(find_set(set3))

    union(set1, set2)
    union(set1, set2)
    print(find_set(set1))
    print(find_set(set2))
    union(set1, set3)
    print(find_set(set3))


if __name__ == '__main__':
    main()