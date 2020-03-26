def is_number(x):
    """ checks if x is a number,
    returns boolean"""
    return isinstance(x, (int, float))

def is_positive(x):
    """ checks if x is a positive number,
    returns boolean"""
    return is_number(x) and x>0

def count(seq, func):
    """ counts how many elements in seq are ints"""
    res = 0
    for elem in seq:
        if func(elem):
            res += 1
    return res
    #count(["a", "B", "c", "a", "d"], (lambda char: char =="a"))
    #count([["a"], [1, 2], ["b", "c"]), (lambda lst: isinstance(lst, list)
    #and len(lst)==2)
    #count([1, 2, 3, 4, 5, 6, 9], (lambda n: n % 3 == 0))

def alt_count(seq, pred):
    """
    Same as count but one line
    """
    return len(list(filter(pred, seq)))

