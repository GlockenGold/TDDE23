def factorial(n, k=False):
    if not k:
        if n <= 1:
            return 1
        else:
            return n * factorial(n - 1)
    elif n == k:
        return 1
    return n * factorial(n - 1, k)
def choose(n, k):
    if k > n-k:
        k = n-k
    return factorial(n, n-k)//factorial(k)

import math

def new_board():
    board = {}
    return board

def reset_board(board):
    board.clear()
    return True

def is_free(board, x, y):
    return (x, y) not in board

def get_piece(board, x, y):
    if not is_free(board, x, y):
        return board[(x, y)]
    else:
        return False

def place_piece(board, x, y, player):
    if not is_free(board, x, y):
        return False
    else:
        board[(x, y)] = player
        return True

def remove_piece(board, x, y):
    if not is_free(board, x, y):
        board.pop((x, y))
        return True
    else:
        return False

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def nearest_piece(board, x, y):
    if get_piece(board, x, y):
        return (x, y)
    elif board == {}:
        return False
    comp = -1
    for coord in board:
        if distance((x, y), coord) <= comp or comp == -1:
            comp = distance((x, y), coord)
            nearest = coord
    return nearest

def move_piece(board, x1, y1, x2, y2):
    if not is_free(board, x1, y1):
        if not is_free(board, x2, y2):
            return False
        else:
            board[(x2, y2)] = board[(x1, y1)]
            remove_piece(board, x1, y1)
            return True
    else:
        return False

def count(board, axis, coord, player):
    counter = 0
    if axis == "row":
        coord_type = 1
    elif axis == "column":
        coord_type = 0
    for elem in board:
        if elem[coord_type] == coord:
            if board[elem] == player:
                counter += 1
    return counter
