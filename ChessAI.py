import chess
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
    def __init__(self, calculation_depth):
        self.calculation_depth = calculation_depth
        self.board = chess.Board()
        self.turn = chess.WHITE

    def calculate_best_move(self, for_black=True):
        return self.minimax(self.board, -float("inf"), float("inf"), self.calculation_depth)

    def make_best_move(self, color):
        if color == chess.WHITE:
            self.board.push(self.minimax(self.board, -float("inf"), float("inf"), self.calculation_depth, False)[1])
        else:
            self.board.push(self.minimax(self.board, -float("inf"), float("inf"), self.calculation_depth)[1])

    def maxi(self, position, depth):
        if depth == 0 or position.is_checkmate():
            return position, evaluate(position)
        else:
            my_max = -float("inf")
            for move in list(position.legal_moves):
                score = self.mini(position.copy().push(chess.Move.from_uci(str(move))), depth - 1)
                if my_max < score:
                    my_max = score

    def mini(self, position, depth):
        if depth == 0 or position.is_checkmate():
            return position, evaluate(position)
        else:
            my_min = float("inf")
            for move in list(position.legal_moves):
                score = self.maxi(position.copy().push(chess.Move.from_uci(str(move))), depth - 1)
                if score < my_min:
                    my_min = score

    def minimax(self, position, alpha, beta, depth, maximizing_for=chess.BLACK):  # is using alpha beta pruning
        if maximizing_for == chess.BLACK:  # maximize for black, minimize for white
            if depth == 0 or position.is_checkmate():
                return evaluate(position), position.move_stack.pop(self.calculation_depth - 1)
            else:
                print(position.turn)
                if position.turn == chess.WHITE:
                    best_move = None
                    for move in list(position.legal_moves):
                        temp_position = position.copy()
                        temp_position.push(chess.Move.from_uci(str(move)))
                        temp_score, temp_move = self.minimax(temp_position, alpha, beta, depth - 1)
                        if alpha < temp_score:
                            alpha = temp_score
                            best_move = temp_move
                            if beta <= alpha:
                                break
                    return alpha, best_move
                else:
                    best_move = None
                    for move in list(position.legal_moves):
                        temp_position = position.copy()
                        temp_position.push(chess.Move.from_uci(str(move)))
                        temp_score, temp_move = self.minimax(temp_position, alpha, beta, depth - 1)
                        if temp_score < beta:
                            beta = temp_score
                            best_move = temp_move
                            if beta <= alpha:
                                break
                    return beta, best_move
        else:  # maximize for white, minimize for black
            if depth == 0 or position.is_checkmate():
                return evaluate(position), position.move_stack.pop(self.calculation_depth - 1)
            else:
                if position.turn == chess.BLACK:
                    best_move = None
                    for move in list(position.legal_moves):
                        temp_position = position.copy()
                        temp_position.push(chess.Move.from_uci(str(move)))
                        temp_score, temp_move = self.minimax(temp_position, alpha, beta, depth - 1)
                        if alpha < temp_score:
                            alpha = temp_score
                            best_move = temp_move
                            if beta <= alpha:
                                break
                    return alpha, best_move
                else:
                    best_move = None
                    for move in list(position.legal_moves):
                        temp_position = position.copy()
                        temp_position.push(chess.Move.from_uci(str(move)))
                        temp_score, temp_move = self.minimax(temp_position, alpha, beta, depth - 1)
                        if temp_score < beta:
                            beta = temp_score
                            best_move = temp_move
                            if beta <= alpha:
                                break
                    return beta, best_move

    # Utility functions

    def load_board(self, new_board):
        self.board = new_board

    def print_board(self):
        print(self.board)

    def get_evaluation(self):
        return evaluate(self.board)
