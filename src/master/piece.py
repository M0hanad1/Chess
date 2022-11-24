class Piece:
    """Chess pieces master class.

        Parameters
        ----------
        position : list[int]
            Piece position on the board [x, y].
        positions_to_move : list[list]
            Positions that the piece can move to [[x, y], [x, y]].
        color : str
            Piece color [white, black].
    """
    POSITIONS_X = ["a", "b", "c", "d", "e", "f", "g", "h"]
    POSITIONS_Y = [1, 2, 3, 4, 5, 6, 7, 8]
    pieces = []

    def __init__(self, position: list[int], positions_to_move: list[list], color: str) -> None:
        self.position = position
        self.available_positions = positions_to_move
        self.color = color
        Piece.pieces.append(self)

    def check_available_positions(self, positions: list[list]) -> None:
        """Check if the positions are available.

        Parameters
        ----------
        positions : list[list]
            All available positions of the piece [[x, y], [x, y]].
        """
        positions_result = positions

        for i in self.pieces:
            if i.position in positions and i.color == self.color:
                positions_result.remove(i.position)

        for i in positions:
            if (i[0] >= 8 or i[0] < 0) or (i[1] >= 8 or i[1] < 0):
                positions_result.remove(i)

        self.available_positions = positions_result