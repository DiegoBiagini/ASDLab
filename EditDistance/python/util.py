import io
import random
import string


# Returns a list of all lines in a file
def get_all_lines(filename):
    file = io.open(filename, "r", encoding="utf8")
    lines = []
    for line in file:
        lines.append(line[:-1])

    file.close()
    return lines


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