# Taken from the evaluation tables in Chess Programming source code
# https://github.com/maksimKorzh/chess_programming/blob/master/src/bbc/move_ordering_intro/bbc.c

import copy

import chess

PAWN = 100
KNIGHT = 300
BISHOP = 350
ROOK = 500
QUEEN = 1000
KING = 10000

PAWN_WHITE = [
    [90, 90, 90, 90, 90, 90, 90, 90],
    [30, 30, 30, 40, 40, 30, 30, 30],
    [20, 20, 20, 30, 30, 30, 20, 20],
    [10, 10, 10, 20, 20, 10, 10, 10],
    [5, 5, 10, 20, 20, 5, 5, 5],
    [0, 0, 0, 5, 5, 0, 0, 0],
    [0, 0, 0, -10, -10, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

PAWN_BLACK = copy.deepcopy(PAWN_WHITE)
PAWN_BLACK.reverse()

KNIGHT_WHITE = [
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 10, 10, 0, 0, -5],
    [-5, 5, 20, 20, 20, 20, 5, -5],
    [-5, 10, 20, 30, 30, 20, 10, -5],
    [-5, 10, 20, 30, 30, 20, 10, -5],
    [-5, 5, 20, 10, 10, 20, 5, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, -10, 0, 0, 0, 0, -10, -5]
]

KNIGHT_BLACK = copy.deepcopy(KNIGHT_WHITE)
KNIGHT_BLACK.reverse()

BISHOP_WHITE = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 10, 10, 0, 0, 0],
    [0, 0, 10, 20, 20, 10, 0, 0],
    [0, 0, 10, 20, 20, 10, 0, 0],
    [0, 10, 0, 0, 0, 0, 10, 0],
    [0, 30, 0, 0, 0, 0, 30, 0],
    [0, 0, -10, 0, 0, -10, 0, 0]
]

BISHOP_BLACK = copy.deepcopy(BISHOP_WHITE)
BISHOP_BLACK.reverse()

ROOK_WHITE = [
    [50, 50, 50, 50, 50, 50, 50, 50],
    [50, 50, 50, 50, 50, 50, 50, 50],
    [0, 0, 10, 20, 20, 10, 0, 0],
    [0, 0, 10, 20, 20, 10, 0, 0],
    [0, 0, 10, 20, 20, 10, 0, 0],
    [0, 0, 10, 20, 20, 10, 0, 0],
    [0, 0, 10, 20, 20, 10, 0, 0],
    [0, 0, 0, 20, 20, 0, 0, 0]
]

ROOK_BLACK = copy.deepcopy(ROOK_WHITE)
ROOK_BLACK.reverse()

QUEEN_WHITE = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

QUEEN_BLACK = copy.deepcopy(QUEEN_WHITE)
QUEEN_BLACK.reverse()

KING_WHITE = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 5, 5, 5, 0, 0],
    [0, 5, 5, 10, 10, 5, 5, 0],
    [0, 5, 10, 20, 20, 10, 5, 0],
    [0, 5, 10, 20, 20, 10, 5, 0],
    [0, 0, 5, 10, 10, 5, 0, 0],
    [0, 5, 5, -5, -5, 0, 5, 0],
    [0, 0, 5, 0, -15, 0, 10, 0]
]

KING_BLACK = copy.deepcopy(KING_WHITE)
KING_BLACK.reverse()

#     (Victims) Pawn Knight Bishop   Rook  Queen   King
#   (Attackers)
#         Pawn   105    205    305    405    505    605
#       Knight   104    204    304    404    504    604
#       Bishop   103    203    303    403    503    603
#         Rook   102    202    302    402    502    602
#        Queen   101    201    301    401    501    601
#         King   100    200    300    400    500    600

MVV_LVA = [
    [105, 205, 305, 405, 505, 605],
    [104, 204, 304, 404, 504, 604],
    [103, 203, 303, 403, 503, 603],
    [102, 202, 302, 402, 502, 602],
    [101, 201, 301, 401, 501, 601],
    [100, 200, 300, 400, 500, 600]
]
