import chess
import chess.svg
import Evaluations


def get_square_score(board, position):
    piece = board.piece_at(position)
    if piece is None:
        return 0
    coefficient = 1

    x = abs(int(position / 8) - 7)
    y = int(position % 8)

    if piece.color == chess.BLACK:
        coefficient = -1

    if piece.piece_type == chess.PAWN:
        if coefficient == 1:
            return coefficient * (Evaluations.PAWN + Evaluations.PAWN_WHITE[x][y])
        else:
            return coefficient * (Evaluations.PAWN + Evaluations.PAWN_BLACK[x][y])
    elif piece.piece_type == chess.KNIGHT:
        if coefficient == 1:
            return coefficient * (Evaluations.KNIGHT + Evaluations.KNIGHT_WHITE[x][y])
        else:
            return coefficient * (Evaluations.KNIGHT + Evaluations.KNIGHT_BLACK[x][y])
    elif piece.piece_type == chess.BISHOP:
        if coefficient == 1:
            return coefficient * (Evaluations.BISHOP + Evaluations.BISHOP_WHITE[x][y])
        else:
            return coefficient * (Evaluations.BISHOP + Evaluations.BISHOP_BLACK[x][y])
    elif piece.piece_type == chess.ROOK:
        if coefficient == 1:
            return coefficient * (Evaluations.ROOK + Evaluations.ROOK_WHITE[x][y])
        else:
            return coefficient * (Evaluations.ROOK + Evaluations.ROOK_BLACK[x][y])
    elif piece.piece_type == chess.QUEEN:
        if coefficient == 1:
            return coefficient * (Evaluations.QUEEN + Evaluations.QUEEN_WHITE[x][y])
        else:
            return coefficient * (Evaluations.QUEEN + Evaluations.QUEEN_BLACK[x][y])
    elif piece.piece_type == chess.KING:
        if coefficient == 1:
            return coefficient * (Evaluations.KING + Evaluations.KING_WHITE[x][y])
        else:
            return coefficient * (Evaluations.KING + Evaluations.KING_BLACK[x][y])


def evaluate(board):
    overall_score = 0
    for i in range(64):
        overall_score += get_square_score(board, i)
    return overall_score


class ChessAI:
    def __init__(self, playing_for=chess.BLACK, calculation_depth=3):
        self.playing_for = playing_for
        self.calculation_depth = calculation_depth
        self.board = chess.Board()
        self.turn = chess.WHITE

    def load_board(self, new_board):
        self.board = new_board

    def print_board(self):
        print(self.board)

    def make_move(self, move):
        self.board.push(move)

    def calculate_score(self):
        return evaluate(self.board)

    def calculate_best_move(self):
        return self.minimax(self.board, self.calculation_depth, True)

    def make_best_move(self):
        self.board.push(self.calculate_best_move()[0])

    def get_board_svg(self, size=350):
        return chess.svg.board(self.board,
                               fill=dict.fromkeys(self.board.attacks(chess.E4), "#cc0000cc"),
                               squares=chess.SquareSet(chess.BB_DARK_SQUARES & chess.BB_FILE_B),
                               size=size)

    def minimax(self, position, depth, alpha=-float("inf"), beta=float("inf"), maximizing=True):
        score_sign = 1  # White
        if self.playing_for == chess.BLACK:
            score_sign = -1  # Black

        if depth == 0 or position.is_checkmate():
            final_evaluation = evaluate(position)
            return position.move_stack[len(position.move_stack) - self.calculation_depth], score_sign * final_evaluation
        else:
            if maximizing:
                max_evaluation = -float("inf")
                move_to_return = None
                for move in list(position.legal_moves):
                    temp_board = position.copy()
                    temp_board.push(chess.Move.from_uci(str(move)))
                    new_position = self.minimax(temp_board, depth - 1, alpha, beta, not maximizing)
                    evaluation = new_position[1]
                    if max_evaluation < evaluation:
                        max_evaluation = evaluation
                        move_to_return = new_position[0]
                    alpha = max(alpha, evaluation)
                    if beta <= alpha:
                        break
                return move_to_return, max_evaluation
            else:
                min_evaluation = float("inf")
                move_to_return = None
                for move in list(position.legal_moves):
                    temp_board = position.copy()
                    temp_board.push(chess.Move.from_uci(str(move)))
                    new_position = self.minimax(temp_board, depth - 1, alpha, beta, not maximizing)
                    evaluation = new_position[1]
                    if evaluation < min_evaluation:
                        min_evaluation = evaluation
                        move_to_return = new_position[0]
                    beta = min(beta, evaluation)
                    if beta <= alpha:
                        break
                return move_to_return, min_evaluation
