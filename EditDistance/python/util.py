import random
import string


# Returns the Jaccard value between 2 sets(lists)
def get_jaccard_value(set1, set2):
    intersection = [value for value in set1 if value in set2]
    union = set().union(set1, set2)

    return len(intersection) / len(union)


# Randomly changes n letters in the passed word
def mistype_word(word, n):
    # Choose which index to change
    chosen_letters = []
    while len(chosen_letters) < n:
        rand = random.randint(0, len(word) - 1)
        if rand not in chosen_letters:
            chosen_letters.append(rand)

    list_string = list(word)
    for letter in chosen_letters:
        list_string[letter] = random.choice(string.ascii_lowercase)

    return "".join(list_string)


# Calls mistype_word on every word in the passed list changing a random number of letters according to word size
# Returns a list of tuples, each tuple contains the correct word and the mistyped word
def mistype_list(words):
    out_list = []
    for word in words:

        if len(word) <= 3:
            n_change = 1
        elif len(word) <= 5:
            n_change = random.randint(1, 2)
        else:
            n_change = random.randint(1, 3)

        out_list.append((word, mistype_word(word, n_change)))

    return out_list


# Returns a list of all lines in a file
def file_to_list(filename):
    with open(filename, "r", encoding="utf8") as file:
        out_list = file.readlines()

    # Remove \n
    return [x.strip() for x in out_list]


# Takes a list of words and adds at the beginning and end of each of them a space
def add_spaces(list):
    list2 = []
    for element in list:
        list2.append(" " + element + " ")

    return list2