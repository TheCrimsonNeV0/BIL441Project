import chess
from ChessAI import ChessAI

puzzle = ChessAI(chess.WHITE, 5)
puzzle.board.set_board_fen("2q1k3/1bQpr3/4p3/8/8/BP6/2P2RPP/5R1K")
print("Puzzle 1: ", puzzle.calculate_best_move())  # Answer: f2f8

puzzle_2 = ChessAI(chess.BLACK, 5)
puzzle_2.board.turn = chess.BLACK
puzzle_2.board.set_board_fen("rnbqkbnr/pppp1ppp/4p3/8/5PP1/8/PPPPP2P/RNBQKBNR")
print("Puzzle 2: ", puzzle_2.calculate_best_move())  # Answer: d8h4

puzzle_3 = ChessAI(chess.WHITE, 5)
puzzle_3.board.set_board_fen("r2qkb1r/ppp1p1pp/2np1n2/4Nb2/3P4/1B6/PPP1PPPP/RNBQK2R")
print("Puzzle 3: ", puzzle_3.calculate_best_move())  # Answer: b3f7
