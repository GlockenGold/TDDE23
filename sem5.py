def is_number(x):
    return isinstance(x, (int, float))

def is_positive(x):
    return is_number(x) and x >= 0

def count(seq, func):
    count = 0
    """Alternativ lösn: return len([item for item in seq if func(item)])"""
    if not seq:
        return 0
    for i in seq:
        if func(i):
            count += 1
    return count
