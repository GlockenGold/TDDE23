def count(seq):
    """
    Counts the number of elements in a given list
    including elements in inner lists
    """

    if not seq:
        return 0
    elif isinstance(seq[0], list):
        return count(seq[0]) + count(seq[1:])
    else:
        return 1 + count(seq[1:])

def test_count():
    test_data = [([], 0), ([1, 2, 3], 3), ([[1, 2], [3]], 3), (["hej"], 1), \
            ([Max_list_djup()] elem_nr)]
    res = []
    for elem in test_data:
        res.append(count(elem[0]) == elem[1])
    return res
