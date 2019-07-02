from ngram import *


def main():
    dictionary = get_all_lines("../dict_nomi_95000.txt")
    print(closest_word_ngram_ed_1gram("cavotto", dictionary, 3))


if __name__ == '__main__':
    main()
