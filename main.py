import chess
from ChessAI import ChessAI

if __name__ == '__main__':
    chess_ai = ChessAI(chess.WHITE, 3)
    chess_ai.make_move(chess.Move.from_uci("e2e4"))
    chess_ai.make_move(chess.Move.from_uci("e7e5"))
    print(chess_ai.board.move_stack)
    print(chess_ai.check_openings())
