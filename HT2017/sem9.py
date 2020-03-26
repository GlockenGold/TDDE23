"""
    Backus-Neur-Form
    S ::= aA | bB
    A ::= aB | e
    B ::= a | b
"""
def S(seq):
    if seq[0] == 'a':
        return A(seq[1:])
    elif seq[0] == 'b':
        return B(seq[1:])
    else:
        return False

def A(seq):
    if not seq:
        return True
    elif seq[0] == 'a':
        return B(seq[1:])
    else:
        return False

def B(seq):
    return seq in ['a', 'b']

