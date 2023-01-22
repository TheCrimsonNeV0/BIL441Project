import chess

from ChessAI import ChessAI

if __name__ == '__main__':
    chess_ai = ChessAI(3)
    chess_ai.make_best_move(chess.WHITE)
    chess_ai.print_board()
    print("\n")