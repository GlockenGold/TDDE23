from labb7b import *

def test_labb7b():
    tree1 = []
    tree2 = [[[2, 8, []], 5, []], 10, [7, 5, 7]]
    tree3 = [5, 10, 15]

    assert contains_key(1, tree1) == False

    assert contains_key(5, tree2) == True

    assert contains_key(10, tree3) == True

    assert contains_key(7, tree3) == False

    assert contains_key(400, tree2) == False

    assert tree_size(tree1) == 0

    assert tree_size(tree2) == 7

    assert tree_size(tree3) == 3

    assert tree_depth(tree1) == 0

    assert tree_depth(tree2) == 4

    assert tree_depth(tree3) == 2
    print("The code passed all tests")
#asd
