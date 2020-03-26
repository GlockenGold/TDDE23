def non_neg(seq1):
    return [x for x in seq1 if x >= 0]

def asciicode(seq2):
    return [ord(x[0]) for x in seq2]

def secondsmallest(seq3):
    """Och en massa till if-statser"""
    return [sort(x)[1] for x in seq3 if len(seq3) >= 2]

def div(seq4):
    return [i for i in range(0,100) if (i%3==0 or i%5==0) and i%15!=0]

def matrix(seq5):
    return [[(1 if x==y else 0) for x in range(0,5)] for y in range(0,5)]

"""
Pseudokod:
    Datatyper: lista av avstånd av typen float
    Funktioner: Skapa resultatlista, addera resultat till resultatlista,
        sortera resultatlista, returnera resultatlista
    Funktionnamn: create_list(), add_result(reslst, *result), list_results(reslst)
    >reslst = create_list()
    >add_result(reslst, 50, 75, 23)
    >list_results(reslst)
    >[23, 50, 75]
"""
def create_list():
    return []

def add_result(reslst, *result):
    for i in result:
        reslst.append(i)
    reslst = reslst.sort()

def return_list(reslst):
    return reslst
