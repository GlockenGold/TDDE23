def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x%y)
    #if y % x == 0: #x != 0
    #    return x
    #else:
    #    return gcd(y%x, x)
