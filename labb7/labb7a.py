def search(pattern, db):
    """ Returns all entries matching pattern in db """
    books = []
    for i in range(len(db)):
        temp = match(db[i], pattern)
        if temp:
            books.append(db[i])

    return books

def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    if not pattern:
        return not seq
    elif isinstance(pattern[0], list):
        if not seq:
            return False
        if isinstance(seq[0], list):
            return match(seq[0], pattern[0]) and match(seq[1:], pattern[1:])
    elif pattern[0] == '--':
        if not seq:
            if len(pattern) == 1:
                return True
            return False
        elif match(seq, pattern[1:]):
            return True
        else:
            return match(seq[1:], pattern)
    elif not seq:
        return False
    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    else:
        return False


db = [[['författare', ['john', 'zelle']],
       ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']], 
       ['år', 2010]],
      [['författare', ['armen', 'asratian']],
       ['titel', ['diskret', 'matematik']],
       ['år', 2012]],
      [['författare', ['j', 'glenn', 'brookshear']],
       ['titel', ['computer', 'science', 'an', 'overview']],
       ['år', 2011]],
      [['författare', ['john', 'zelle']],
       ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], 
       ['år', 2009]],
      [['författare', ['anders', 'haraldsson']],
       ['titel', ['programmering', 'i', 'lisp']],
       ['år', 1993]]]
