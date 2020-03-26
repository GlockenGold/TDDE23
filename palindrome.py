def palin_rec(seq):
    if not seq:
        return True
    elif seq[0] == seq[-1]:
        return palin_rec(seq[1:-1])
    else:
        return False
def palin_super(seq):
    return string == string[::-1]
