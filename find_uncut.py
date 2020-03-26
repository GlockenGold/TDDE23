def find_uncut(map):
    result = []
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if not map[y][y]:
                result.append((x, y))
    return result

def find_uncut2(map):
     result = [(x,y) for y in range(0, len(map)) for x in range(0, len(map[y])) if not map[x][y]]
     return result
