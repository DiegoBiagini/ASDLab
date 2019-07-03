# Node of a set, size is set only for the representative
class Node:
    def __init__(self, value, representative, next, size, last):
        self.value = value
        self.representative = representative
        self.next = next
        self.size = size
        self.last = last


# A set is identified by a 2 element list containing the head of the set and the number of elements
def make_set(value):
    first_node = Node(value, None, None, 1, None)
    first_node.representative = first_node
    first_node.last = first_node
    return first_node


# Returns the representative
def find_set(node):
    return node.representative


# Joins together two sets using weighted union
def union(set1, set2):
    set1rep = find_set(set1)
    set2rep = find_set(set2)

    # Check if they are different sets
    if set1rep == set2rep:
        return set1

    size1 = set1rep.size
    size2 = set2rep.size

    if size1 < size2:
        # Concatenate 1 to 2
        bigger_set = set2rep
        smaller_set = set1rep
    else:
        # Concatenate 2 to 1
        bigger_set = set1rep
        smaller_set = set2rep

    # Concatenate smaller to bigger
    bigger_set.last.next = smaller_set

    # Set the representative of the smaller set
    smaller_set.representative = bigger_set
    smaller_nodes = smaller_set

    while smaller_nodes.next is not None:
        smaller_nodes = smaller_nodes.next
        smaller_nodes.representative = bigger_set

    # Set the last to the last of the smaller set
    bigger_set.last = smaller_nodes
    bigger_set.size = size1 + size2

    return bigger_set

