import io


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