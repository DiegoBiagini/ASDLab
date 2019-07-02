from editdistance import *
from util import *


# Returns a list of strings containing all the n-grams of the given string
def get_ngram(word, n):
    if n < 1:
        return []
    return [word[i: n + i] for i in range(0, len(word) + 1 - n)]


# Takes the list that contains the words(dictionary) and the n-grams to create
# returns a list of tuples, each tuple contains the original word and the list of its n-grams
# ex: [ ("ciao", ["ci","ia","ao"]) , (...,[...]), ...]
def dictionary_ngram(dictionary, n):
    result = []
    for line in dictionary:
        ngram = get_ngram(line, n)
        result.append((line, ngram))

    return result


# Finds the closest word in the dictionary using intersection of n-grams, executes edit distance only if the Jaccard
# coefficient is over a certain threshold
def closest_word_ngram_ed_jacc(word, dictionary, n, jaccard):
    all_ngrams = dictionary_ngram(dictionary, n)
    word_ngram = get_ngram(word, n)

    mindistance = np.inf
    closest = ""
    # Check all words
    for entry in all_ngrams:
        # If jaccard values is over threshold calculate edit distance
        if get_jaccard_value(word_ngram, entry[1]) > jaccard:
            distance = edit_distance(word, entry[0])

            if distance < mindistance:
                closest = entry[0]
                mindistance = distance

    return closest, mindistance


# Finds the closest word in the dictionary using intersection of n-grams, executes edit distance only there is at least
# a common n-gram
def closest_word_ngram_ed_1gram(word, dictionary, n):
    all_ngrams = dictionary_ngram(dictionary, n)
    word_ngram = get_ngram(word, n)

    mindistance = np.inf
    closest = ""
    # Check all words
    for entry in all_ngrams:
        # If intersection size is at least one
        if len([value for value in word_ngram if value in entry[1]]):
            distance = edit_distance(word, entry[0])

            if distance < mindistance:
                closest = entry[0]
                mindistance = distance

    return closest, mindistance


# Finds the closest word in the dictionary using only intersection of ngrams, finds the word with the biggest Jaccard
# coefficient
def closest_word_ngram_int(word, dictionary, n):
    all_ngrams = dictionary_ngram(dictionary, n)
    word_ngram = get_ngram(word, n)

    minjacc = -1
    closest = ""
    # Check all words
    for entry in all_ngrams:
        jaccard = get_jaccard_value(word_ngram, entry[1])
        if jaccard > minjacc:
            minjacc = jaccard
            closest = entry[0]

    return closest, minjacc

