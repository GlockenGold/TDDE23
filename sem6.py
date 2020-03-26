def count(seq):
    """
        Counts the number of elements in a given list including elements in inner lists
    """
    if not seq:
        return 0
    elif isinstance(seq[0], list):
        return count(seq[0]) + count(seq[1:])
    else:
        return 1 + count(seq[1:])

def test_count():
    """ Jätte, jätte, jättedålig kod """
    test_cases = [[0,1, "a"], [], [["hej"], 6, "b"], [[[[["Bu"]]]], 3, 2], ([1, 2], 2)]
    res = 0

    for elem in test_cases:
        res += count(elem)
    return res

