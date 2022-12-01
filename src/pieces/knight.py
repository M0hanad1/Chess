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
        """Get the available positions for the Knight to move to.

        Returns
        -------
        list[list[int]]
            Available positions for the Knight to move to.
        """
        # All the available positions to move to.
        all_available_positions = [
            [self.position[0]+2, self.position[1]+1], [self.position[0]-2, self.position[1]+1], # 2Right 1Up, 2Left 1Up.
            [self.position[0]+2, self.position[1]-1], [self.position[0]-2, self.position[1]-1], # 2Right 1Down, 2Left 1Down.
            [self.position[0]+1, self.position[1]+2], [self.position[0]+1, self.position[1]-2], # 2Up 1Right, 2Down 1Right.
            [self.position[0]-1, self.position[1]+2], [self.position[0]-1, self.position[1]-2], # 2Up 1Left, 2Down 1Left.
        ]
        available_positions = all_available_positions.copy()

        for i in all_available_positions:
            # Check if [the position is available on the board, there's no piece from the same color in this position].
            try:
                if (position_on_board := self.board[self.convert_to_letters(i)]) and position_on_board.color == self.color: # Check if there's a piece on this position with the same color.
                    available_positions.remove(i) # Remove the position.

            except IndexError: # Position not available on the board.
                available_positions.remove(i)

        return available_positions
