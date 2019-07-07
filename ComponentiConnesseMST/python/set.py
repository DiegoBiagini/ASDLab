# Node of a tree that represents a set
class Node:
    def __init__(self, value, father, rank):
        self.value = value
        self.father = father
        self.rank = rank
        self.sons = []


# Create the tree with rank = 0
def make_set(value):
    node = Node(value, None, 0)
    node.father = node
    return node


# Joins together 2 trees
def link(x, y):
    if x.rank > y.rank:
        y.father = x
        x.sons.append(y)
    else:
        x.father = y
        y.sons.append(x)
        if x.rank == y.rank:
            y.rank += 1

    return find_set(x)


# Goes up the tree and simplifies the tree using path compression
def find_set(node):
    if node != node.father:
        first_father = find_set(node.father)

        # Update the sons of the father
        if node.father != first_father:
            node.father = first_father
            node.father.sons.append(node)
            node.father.sons += node.sons

    return node.father


# Joins together two sets
def union(set1, set2):
    return link(find_set(set1), find_set(set2))


# Returns a list containing the values in the set
def set_to_list(set):
    # After the find set there will only be a father with n - 1 sons
    first_father = find_set(set)
    list = []
    list.append(first_father.value)
    for son in first_father.sons:
            list.append(son.value)

    return list
