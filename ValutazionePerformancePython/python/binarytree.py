# Implementation of ABR
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def get(self):
        return self.key

    def set(self, key):
        self.key = key

    def get_children(self):
        children = []
        if not(self.left is None):
            children.append(self.left)
        if not(self.right is None):
            children.append(self.right)
        return children


class ABR:
    def __init__(self):
        self.root = None

    def set_root(self, key):
        self.root = Node(key)

    def insert(self, key):
        if self.root is None:
            self.set_root(key)
        else:
            self.insert_node(self.root, key)

    def insert_node(self, current_node, key):
        if key <= current_node.key:
            if current_node.left:
                self.insert_node(current_node.left, key)
            else:
                current_node.left = Node(key)

        elif key > current_node.key:
            if current_node.right:
                self.insert_node(current_node.right, key)
            else:
                current_node.right = Node(key)

    def find(self, key):
        return self.find_node(self.root, key)

    def find_node(self, current_node, key):
        # Found
        if current_node is None:
            return False
        # Not found
        elif key == current_node.key:
            return True

        # Go down
        elif key < current_node.key:
            return self.find_node(current_node.left, key)
        else:
            return self.find_node(current_node.right, key)

    # Returns a list with the keys of the nodes that were visited( following this visit order)
    def post_order_visit(self):
        def _post_order(v, list):
            if v is None:
                return
            if v.left is not None:
                _post_order(v.left, list)
            if v.right is not None:
                _post_order(v.right, list)
            list.append(v.key)

        explore_list = []
        _post_order(self.root, explore_list)
        return explore_list
