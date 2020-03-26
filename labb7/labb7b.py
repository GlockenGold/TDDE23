from tree import *

def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn):
    """ """
    if is_empty_tree(tree):
        return empty_tree_fn()
    elif is_leaf(tree):

        return leaf_fn(tree)
    else:
        #looks weird but calls inner_node_fn with key, traverse on left and
        # right subtree
        return inner_node_fn(key(tree), \
                             traverse(left_subtree(tree), \
                                      inner_node_fn, leaf_fn, \
                                      empty_tree_fn), \
                             traverse(right_subtree(tree), \
                                      inner_node_fn, leaf_fn, \
                                      empty_tree_fn))


def contains_key(key, tree):
    """ Traverses a tree and checks if the tree contains key. Returns true
    if it found the key otherwise false. """
    def empty_tree():
        return False

    def leaf(k):
        return k == key

    def inner_node(k, left, right):
        return k == key or left or right

    return traverse(tree, inner_node, leaf, empty_tree)


def tree_size(tree):
    """ Counts and returns the size (number of leafs and key nodes) of tree """
    def empty_tree():
        return 0

    def leaf(key):
        return 1

    def inner_node(key, left, right):
        return 1 + left + right

    return traverse(tree, inner_node, leaf, empty_tree)


def tree_depth(tree):
    """ Calculates and returns the highest depth of tree. """
    def empty_tree():
        return 0

    def leaf(key):
        return 1

    def inner_node(key, left, right):
        return 1 + max(left, right)

    return traverse(tree, inner_node, leaf, empty_tree)
