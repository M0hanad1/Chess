from src.master.piece import Piece


class Knight(Piece):
    """Knight piece class.

        Parameters
        ----------
        position : list[int]
            Knight position on the board.
        available_positions : list[list[int]]
            Available positions for the Knight to move to.
        color : str
            Knight color.
    """
    def __init__(self, position: list[int], available_positions: list[list[int]], color: str) -> None:
        super().__init__(position, available_positions, color)

    def get_available_position(self) -> list[list[int]]:
        """Get all the available positions for the Knight.

        Returns
        -------
        list[list[int]]
            Available positions for the Knight to move to.
        """
        return self.check_available_positions([
            [self.position[0]+2, self.position[1]+1], [self.position[0]-2, self.position[1]+1], # 2Right 1Up, 2Left 1Up.
            [self.position[0]+2, self.position[1]-1], [self.position[0]-2, self.position[1]-1], # 2Right 1Down, 2Left 1Down.
            [self.position[0]+1, self.position[1]+2], [self.position[0]+1, self.position[1]-2], # 2Up 1Right, 2Down 1Right.
            [self.position[0]-1, self.position[1]+2], [self.position[0]-1, self.position[1]-2], # 2Up 1Left, 2Down 1Left.
        ])

    def check_available_positions(self, positions: list[list[int]]) -> list[list[int]]:
        """Check if the positions are available.

        Parameters
        ----------
        positions : list[list[int]]
            All available positions of the Knight.

        Returns
        -------
        list[list[int]]
            Available positions for the Knight to move to.
        """
        positions_result = positions.copy()

        for i in positions:
            # Check if [the position is available on the board, there's no piece from the same color in this position]
            if not (position_in_letters := self.convert_to_letters(i)) or (self.board[position_in_letters] and self.board[position_in_letters].color == self.color):
                positions_result.remove(i)

        return positions_result
