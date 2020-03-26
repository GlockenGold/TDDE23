def rmax3(x, y, z):
    if x >= y:
        if z >= x:
            return z
        else:
            return x
    else:
        if z >= y:
            return z
        else:
            return y
