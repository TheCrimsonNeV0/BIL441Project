import chess
import Evaluations


class ChessAI:
    def __init__(self, calculation_depth):
        self.calculation_depth = calculation_depth
        self.board = chess.Board()

    def evaluate(self):
        overall_score = 0
        for i in range(64):
            overall_score += self.get_square_score(i)
        return overall_score

    # Utility Functions
    def get_square_score(self, position):
        piece = self.board.piece_at(position)
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

    def minimax(self, alpha, beta):
        pass









