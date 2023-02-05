import os
import time
import chess
from ChessAI import ChessAI

if __name__ == '__main__':
    chess_ai = ChessAI(chess.BLACK, 5)

    while not chess_ai.board.is_checkmate():
        board_svg = chess_ai.get_board_svg()
        with open('chess.svg', 'w') as output_file:
            output_file.write(board_svg)
        time.sleep(0.1)
        os.startfile('chess.svg')

        print(chess_ai.board.legal_moves)

        print("Evaluation: ", chess_ai.calculate_score())
        player_move = input("Input move (in uci format): ")
        chess_ai.make_move(chess.Move.from_uci(player_move))

        board_svg = chess_ai.get_board_svg()
        with open('chess.svg', 'w') as output_file:
            output_file.write(board_svg)
        time.sleep(0.1)
        os.startfile('chess.svg')

        ai_best_move = chess_ai.make_best_move()
        print(ai_best_move)
