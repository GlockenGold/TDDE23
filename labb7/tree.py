# encoding: iso-8859-1

# TDDD73 Lab 3, binary tree

def is_empty_tree(tree):
    return isinstance(tree, list) and not tree


def is_leaf(tree):
    return isinstance(tree, int)


def create_tree(left_tree, key, right_tree):
    return [left_tree, key, right_tree]


def left_subtree(tree):
    return tree[0]


def right_subtree(tree):
    return tree[2]


def key(tree):
    return tree[1]
