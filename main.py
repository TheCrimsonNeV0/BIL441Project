import chess
from ChessAI import ChessAI

if __name__ == '__main__':
    chess_ai = ChessAI(chess.BLACK, 3)
    while not chess_ai.board.is_checkmate():
        chess_ai.print_board()
        player_move = input("Input move (in uci format): ")
        chess_ai.make_move(chess.Move.from_uci(player_move))
        chess_ai.make_best_move()
