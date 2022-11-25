from src.master.piece import Piece


class Rook(Piece):
    """Rook piece class.

        Parameters
        ----------
        position : list[int]
            Rook position on the board.
        available_positions : list[list[int]]
            Available positions for the Rook to move to.
        color : str
            Rook color.
    """
    def __init__(self, position: list[int], available_positions: list[list[int]], color: str) -> None:
        super().__init__(position, available_positions, color)

    def get_available_position(self) -> list[list[int]]:
        """Get all the available positions for the Rook.

        Returns
        -------
        list[list[int]]
            Available positions for the Rook to move to.
        """
        pass
