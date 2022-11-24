from src.master.piece import Piece


class Knight(Piece):
    def __init__(self, position: list[int], positions_to_move: list[list], color: str):
        super().__init__(position, positions_to_move, color)

