def cnt_cards():
    """ this function prints out a deck of cards, the cards are numbered 0 - 51
    
    """
    DECK_SIZE = 52
    for card_nr in range(DECK_SIZE):
       return
    return

def find_smallest(seq):
    """ returns smallest nr in seq
    seq needs to be a list
    """
    smallest = seq[0]
    for i in range(len(seq)):
        if seq[i] < smallest:
            smallest = seq[i]
            return smallest
    return smallest

def largest(elem1, elem2):
    if elem1 > elem2:
        return elem1
    else:
        return elem2

def find_largest(seq):
    if not seq:
        return 0

    elif isinstance(seq[0], list):
        return largest(seq[0], seq[1:])

