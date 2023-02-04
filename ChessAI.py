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
        else:  # Quiet Moves
            # Rules to rate quiet moves
            # 1 - Develop minor pieces -> Already in board evaluation
            # 2 - Connect rooks
            # 3 - Activate pawns to promote
            # 4 - Activate pieces

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
        return self.minimax(self.board, self.calculation_depth, True)[0]

    def make_best_move(self):
        best_move_opening = self.check_openings()
        if len(best_move_opening) == 0:
            best_move = self.calculate_best_move()
        else:
            if self.playing_for == chess.WHITE:
                best_move = best_move_opening[0][0]
            else:
                best_move = best_move_opening[len(best_move_opening) - 1][0]

        self.board.push(best_move)
        return best_move

    def get_board_svg(self, size=350):
        return chess.svg.board(self.board, size=size)

    def check_openings(self):
        openings = Openings.OPENINGS
        possible_openings = []
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
                    temp_move = chess.Move.from_uci(str(opening.opening.split(" ")[move_index]))
                    if temp_move not in possible_openings:
                        temp_board = self.board.copy()
                        temp_board.push(temp_move)
                        possible_openings.append((temp_move, evaluate(temp_board)))
        sorted_moves = sorted(possible_openings, key=lambda x: x[1], reverse=True)
        return sorted_moves

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

                    if max_evaluation < evaluation:
                        max_evaluation = evaluation
                        move_to_return = new_position[0]
                    alpha = max(alpha, max_evaluation)
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
                    if evaluation < min_evaluation:
                        min_evaluation = evaluation
                        move_to_return = new_position[0]
                    beta = min(beta, min_evaluation)
                    if beta <= alpha:
                        break
                return move_to_return, min_evaluation
