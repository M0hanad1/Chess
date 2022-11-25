class Piece:
    """Chess pieces master class.

        Parameters
        ----------
        position : list[int]
            Piece position on the board.
        available_positions : list[list[int]]
            Available positions for the Piece to move to.
        color : str
            Piece color.
    """
    POSITIONS_X = ["a", "b", "c", "d", "e", "f", "g", "h"]
    POSITIONS_Y = ["1", "2", "3", "4", "5", "6", "7", "8"]
    board = {
        'a1': None, 'a2': None, 'a3': None, 'a4': None, 'a5': None, 'a6': None, 'a7': None, 'a8': None,
        'b1': None, 'b2': None, 'b3': None, 'b4': None, 'b5': None, 'b6': None, 'b7': None, 'b8': None,
        'c1': None, 'c2': None, 'c3': None, 'c4': None, 'c5': None, 'c6': None, 'c7': None, 'c8': None,
        'd1': None, 'd2': None, 'd3': None, 'd4': None, 'd5': None, 'd6': None, 'd7': None, 'd8': None,
        'e1': None, 'e2': None, 'e3': None, 'e4': None, 'e5': None, 'e6': None, 'e7': None, 'e8': None,
        'f1': None, 'f2': None, 'f3': None, 'f4': None, 'f5': None, 'f6': None, 'f7': None, 'f8': None,
        'g1': None, 'g2': None, 'g3': None, 'g4': None, 'g5': None, 'g6': None, 'g7': None, 'g8': None,
        'h1': None, 'h2': None, 'h3': None, 'h4': None, 'h5': None, 'h6': None, 'h7': None, 'h8': None
        }
    pieces = []

    def __init__(self, position: list[int], available_positions: list[list[int]], color: str) -> None:
        self.position = position
        self.position_letters = self.convert_to_letters(position)
        self.available_positions = available_positions
        self.color = color
        Piece.pieces.append(self)
        Piece.board[self.position_letters] = self

    @staticmethod
    def convert_to_letters(position: list[int]) -> str:
        """Convert position from int to letters.

        Parameters
        ----------
        position : list[int]
            Position to convert from.

        Returns
        -------
        str
            Position in letters.
        """
        try:
            return Piece.POSITIONS_X[position[0]]+Piece.POSITIONS_Y[position[1]]

        except IndexError:
            return

    def change_position(self, new_position: list[int]) -> None:
        """Change the Piece position.

        Parameters
        ----------
        new_position : list[int]
            New position to change to.
        """
        self.position = new_position

    def change_available_positions(self, new_available_positions: list[list[int]]) -> None:
        """Change the Piece available positions.

        Parameters
        ----------
        new_available_positions : list[list[int]]
            New available positions to change to.
        """
        self.available_positions = new_available_positions

    def remove_piece(self) -> None:
        """Remove the Piece from the game.
        """
        self.board[self.position_letters] = None
        self.pieces.remove(self)
        del self
