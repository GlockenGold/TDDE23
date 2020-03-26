from copy import deepcopy
res = []

# Uppgift 1 #
def collatz(num):
    res = [num]
    while num > 1:
        if num % 2 == 0:
            res.append(num//2)
            num = num//2
        else:
            res.append(num*3+1)
            num = num*3+1
    return res

# Uppgift 2 #
def reverse_i(seq):
    res = []
    seq_copy = deepcopy(seq)
    while len(seq_copy) > 0:
        res.append(seq_copy[-1])
        seq_copy.pop()
    return res

def reverse_r(seq):
    org = deepcopy(seq)
    global res
    if len(org) >= 1:
        res.append(org[-1])
        org = org[:-1]
        return reverse_r(org)
    return res

# Uppgift 3 #
def add_for_each(seq, func):
    res = 0
    for elem in seq:
        res += func(elem)
    return res

def average_max(seq):
    res = 0
    for elem in seq:
        res += add_for_each(elem, lambda x: x)/len(elem)
    print(res)


# Uppgift 4 #
def palindrom(seq):
    for i in range(len(seq)//2):
        if isinstance(i, list):
            print("hej")
        elif seq[i] != seq[-1-i]:
            return False
    return True

