import chess
import chess.svg
import Evaluations
import Openings


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


def sort_moves(position):
    sorted_moves = []
    captures = []
    quiet_moves = []
    for move in list(position.legal_moves):
        if position.is_capture(move):  # Capture
            attacker = position.piece_at(move.from_square).piece_type
            if position.is_en_passant(move):
                victim = chess.PAWN
            else:
                victim = position.piece_at(move.to_square).piece_type
            score = Evaluations.MVV_LVA[attacker - 1][victim - 1] + 10000  # For killer moves
            captures.append([move, score])
        else:  # Quiet Move
            quiet_moves.append([move, 0])

    sorted_captures = sorted(captures, key=lambda x: x[1], reverse=True)
    for i in sorted_captures:
        sorted_moves.append(i[0])
    for i in quiet_moves:
        sorted_moves.append(i[0])
    return sorted_moves


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
        best_move = self.check_openings()
        if best_move is None:
            best_move = self.calculate_best_move()[0]
        self.board.push(best_move)
        return best_move

    def get_board_svg(self, size=350):
        return chess.svg.board(self.board,
                               fill=dict.fromkeys(self.board.attacks(chess.E4), "#cc0000cc"),
                               squares=chess.SquareSet(chess.BB_DARK_SQUARES & chess.BB_FILE_B),
                               size=size)

    def check_openings(self):
        openings = Openings.FOR_WHITE
        if self.playing_for == chess.BLACK:
            openings = Openings.FOR_BLACK

        for opening in openings:
            if len(opening.opening.split(" ")) <= len(self.board.move_stack):
                continue
            else:
                opening_played = True
                move_index = 0
                try:
                    for i in range(len(self.board.move_stack)):
                        if str(self.board.move_stack[i]) != opening.opening.split(" ")[i]:
                            opening_played = False
                            raise StopIteration
                        move_index += 1
                except StopIteration:
                    pass
                if opening_played:
                    return chess.Move.from_uci(str(opening.opening.split(" ")[move_index]))
        return None

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
                for move in sort_moves(position):
                    temp_board = position.copy()
                    temp_board.push(chess.Move.from_uci(str(move)))
                    new_position = self.minimax(temp_board, depth - 1, alpha, beta, not maximizing)
                    evaluation = new_position[1]

                    # if beta <= evaluation:
                    #     pass

                    if max_evaluation < evaluation:  # Fail alpha-beta cutoff
                        max_evaluation = evaluation
                        move_to_return = new_position[0]
                    alpha = max(alpha, evaluation)
                    if beta <= alpha:
                        break
                return move_to_return, max_evaluation
            else:
                min_evaluation = float("inf")
                move_to_return = None
                for move in sort_moves(position):
                    temp_board = position.copy()
                    temp_board.push(chess.Move.from_uci(str(move)))
                    new_position = self.minimax(temp_board, depth - 1, alpha, beta, not maximizing)
                    evaluation = new_position[1]
                    if evaluation < min_evaluation:  # Fail alpha-beta cutoff
                        min_evaluation = evaluation
                        move_to_return = new_position[0]
                    beta = min(beta, evaluation)
                    if beta <= alpha:
                        break
                return move_to_return, min_evaluation
