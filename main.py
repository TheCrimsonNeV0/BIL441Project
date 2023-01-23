import chess

from ChessAI import ChessAI

if __name__ == '__main__':
    chess_ai = ChessAI(5)
    print(chess_ai.calculate_best_move()[0])
    print(chess_ai.calculate_best_move()[1])
    # chess_ai.make_best_move()
    chess_ai.print_board()
    print("\n")