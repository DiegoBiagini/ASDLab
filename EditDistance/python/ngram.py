import io


# Returns a list of strings containing all the n-grams of the given string
def get_ngram(word, n):
    if n < 1:
        return []
    return [word[i: n + i] for i in range(0, len(word) + 1 - n)]


# Takes the name of the dictionary to open, the n-grams to create
# returns a list of tuples, each tuple contains the original word and the list of its n-grams
# ex: [ ("ciao", ["ci","ia","ao"]) , (...,[...]), ...]
def dictionary_ngram(filename, n):
    lines = get_all_lines(filename)
    result = []
    for line in lines:
        ngram = get_ngram(line, n)
        result.append((line, ngram))

    return result


# Returns a list of all lines in a file
def get_all_lines(filename):
    file = io.open(filename, "r", encoding="utf8")
    lines = []
    for line in file:
        lines.append(line[:-1])

    file.close()
    return lines
