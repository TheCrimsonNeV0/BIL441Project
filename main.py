import chess
from ChessAI import ChessAI

if __name__ == '__main__':
    chess_ai = ChessAI(chess.BLACK, 5)

    while not chess_ai.board.is_checkmate():
        chess_ai.print_board()
        print("Evaluation: ", chess_ai.calculate_score())
        for item in chess_ai.board.generate_legal_captures():
            print(item)
        player_move = input("Input move (in uci format): ")
        chess_ai.make_move(chess.Move.from_uci(player_move))
        chess_ai.make_best_move()
