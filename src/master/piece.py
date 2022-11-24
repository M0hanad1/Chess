class Piece:
    POSITIONS_X = ["a", "b", "c", "d", "e", "f", "g", "h"]
    POSITIONS_Y = [1, 2, 3, 4, 5, 6, 7, 8]
    pieces = []
    """Chess pieces master class.

        Args:
            position (list[int]): Piece position on the board [x, y].
            positions_to_move (list[list]): Positions that the piece can move to.
            color (str): Piece color [white, black]."""

    def __init__(self, position: list[int], positions_to_move: list[list], color: str) -> None:
        self.position = position
        self.positions_to_move = positions_to_move
        self.color = color
        Piece.pieces.append(self)

    def check_position_available(self, positions: list[list]) -> bool:
        for i in self.pieces:
            if i.position in positions:
                return False

        for i in positions:
            if i[0] >= len(self.POSITIONS_X) or i[1] >= len(self.POSITIONS_Y):
                return False

        return True