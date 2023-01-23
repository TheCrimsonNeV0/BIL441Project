import chess
from ChessAI import ChessAI

if __name__ == '__main__':
    chess_ai = ChessAI(chess.BLACK, 3)
    chess_ai.board.push(chess.Move.from_uci(str("e2e4")))
    chess_ai.print_board()
    print("")

    chess_ai.board.push(chess.Move.from_uci(str("d7d5")))
    chess_ai.print_board()
    print("")

    chess_ai.board.push(chess.Move.from_uci(str("g1f3")))
    chess_ai.print_board()
    print("")

    chess_ai.make_best_move()
    chess_ai.print_board()
    print("\nCurrent score: ", chess_ai.calculate_score())
