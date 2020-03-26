def power(x, y):
    result = x
    for i in range(y-1):
        result = result * x
    return result
