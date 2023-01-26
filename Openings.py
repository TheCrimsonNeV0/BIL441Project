class Opening:
    def __init__(self, opening, evaluation):
        self.opening = opening
        self.evaluation = evaluation


ITALIAN_OPENING_1 = Opening("e2e4 e7e5 g1f3 b8c6 f1c4 f8c5", 0.2)  # Giuoco Piano | Stockfish Evaluation: +0.2
ITALIAN_OPENING_2 = Opening("e2e4 e7e5 g1f3 b8c6 f1c4 g8f6", 0.3)  # Two Knights Defense | Stockfish Evaluation: +0.3

RUY_LOPEZ_OPENING_1 = Opening("e2e4 e7e5 g1f3 b8c6 f1b5 g8f6", 0.3)  # Berlin Defense | Stockfish Evaluation: +0.3
RUY_LOPEZ_OPENING_2 = Opening("e2e4 e7e5 g1f3 b8c6 f1b5 a7a6", 0.4)  # Morphy Defense | Stockfish Evaluation: +0.4

CARO_KANN_OPENING_1 = Opening("e2e4 c7c6 d2d4 d7d5 e4d5 c6d5", 0.3)  # Exchange Variation | Stockfish Evaluation: +0.3
CARO_KANN_OPENING_2 = Opening("e2e4 c7c6 g1f3 d7d5 b1c3 c8g4", 0.4)  # Nf3 Defense | Stockfish Evaluation: +0.4

QUEENS_GAMBIT_DECLINED = Opening("d2d4 d7d5 c2c4 e7e6 b1c3 g8f6", 0.4)  # Stockfish Evaluation: +0.4
QUEENS_GAMBIT_ACCEPTED = Opening("d2d4 d7d5 c2c4 d5c4 e2e4 g8f6", 0.5)  # Stockfish Evaluation: +0.5

INDIAN_DEFENSE = Opening("d2d4 g8f6 c2c4 e7e6 g1f3 d7d5", 0.4)  # Ends up in the same position with Queens Gambit Declined | Stockfish Evaluation: +0.4

LONDON_SYSTEM_GAMBIT_DECLINED = Opening("d2d4 d7d5 c1f4 c7c5 e2e3 b8c6", 0.0)  # Steinitz Gambit Declined | Stockfish Evaluation: 0.0
LONDON_SYSTEM_GAMBIT_ACCEPTED = Opening("d2d4 d7d5 c1f4 c7c5 d4c5 e7e6", 0.0)  # Steinitz Gambit Accepted | Stockfish Evaluation: 0.0

ALEKHINE_DEFENSE = Opening("e2e4 b8c6 e4e5 f6d5 d2d4 d7d6", 0.8)  # Normal Variation | Stockfish Evaluation: +0.8

FRENCH_DEFENSE = Opening("e2e4 e7e6 d2d4 d7d5 e4d5 e6d5", 0.2)  # Exchange Variation | Stockfish Evaluation: +0.2

# Openings should be sorted by quality and be in descending order
OPENINGS = [ITALIAN_OPENING_1, ITALIAN_OPENING_2, RUY_LOPEZ_OPENING_1, RUY_LOPEZ_OPENING_2, CARO_KANN_OPENING_1,
            CARO_KANN_OPENING_2, QUEENS_GAMBIT_DECLINED, QUEENS_GAMBIT_ACCEPTED, INDIAN_DEFENSE,
            LONDON_SYSTEM_GAMBIT_DECLINED, LONDON_SYSTEM_GAMBIT_ACCEPTED, ALEKHINE_DEFENSE, FRENCH_DEFENSE]

FOR_WHITE = sorted(OPENINGS, key=lambda x: x.evaluation, reverse=False)
FOR_BLACK = sorted(OPENINGS, key=lambda x: x.evaluation, reverse=True)
