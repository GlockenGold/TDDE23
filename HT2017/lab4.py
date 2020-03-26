"""
Lab 4 A
"""
def split_rec(seq):
    first = ""
    second = ""
    if seq == "":
        return (first, second)
    first, second = split_rec(seq[1:])
    if seq[0].isupper() or seq[0].isspace() or seq[0] == "|":
        return (first, seq[0]+ second)
    elif seq[0].islower() or seq[0] == "_" or seq[0] == ".":
        return (seq[0] + first, second)
    else:
        return (first, second)

def split_it(seq):
    first = ""
    second = ""
    for x in seq:
        if x.islower() or x == "_" or x == ".":
            first += x
        elif x.isupper() or x.isspace() or x == "|":
            second += x
    return (first, second)

"""
Lab 4 B
"""
def interpret(prep, prep_dict):
    if not isinstance(prep, list):
        if prep == "true":
            return prep
        elif prep == "false":
            return prep
        prep = prep_dict[prep]
        return prep
    if len(prep) < 3:
        return not_operator(prep, prep_dict)
    elif prep[0] == "NOT":
        return not_operator(prep[0], prep_dict)
    elif prep[1] == "AND":
        return and_operator(prep, prep_dict)
    return or_operator(prep, prep_dict)

def _and_(prep1, prep2):
    if not isinstance(prep1, list):
        return "true" if prep1 == "true" and prep2 == "true" else "false"
    else:
        return "true" if prep1[0] == "true" and prep1[2] == "true" else "false"

def and_operator(prep, prep_dict):
    if not isinstance(prep[0], list):
        if not isinstance(prep[2], list):
            if prep[0] in prep_dict:
                prep[0] = prep_dict[prep[0]]
            if prep[2] in prep_dict:
                prep[2] = prep_dict[prep[2]]
        return _and_(prep, prep)
    return _and_(interpret(prep[0], prep_dict), interpret(prep[2], prep_dict))

def _or_(prep1, prep2):
    if not isinstance(prep1, list):
        return "true" if prep1 == "true" or prep2 == "true" else "false"
    else:
        return "true" if prep1[0] == "true" or prep1[2] == "true" else "false"

def or_operator(prep, prep_dict):
    if not isinstance(prep[2], list):
        if prep[0] in prep_dict:
            prep[0] = prep_dict[prep[0]]
        if prep[2] in prep_dict:
            prep[2] = prep_dict[prep[2]]
        return _or_(prep, prep)

    return _or_(interpret(prep[0], prep_dict), interpret(prep[2], prep_dict))

def _not_(prep):
    return "false" if prep == "true" else "true"

def not_operator(prep, prep_dict):
    if not isinstance(prep[1], list):
        if prep[1] in prep_dict:
            prep[1] = prep_dict[prep[1]]
        return _not_(prep[1])
    return _not_(interpret(prep[1], prep_dict))
