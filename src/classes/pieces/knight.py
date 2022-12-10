from src.classes.master.piece import Piece


class Knight(Piece):
    '''Knight piece class.

        Parameters
        ----------
        position : :class:`list`
            Knight position on the board.
        available_positions : :class:`list`
            Available positions for the Knight to move to.
        COLOR : :class:`str`
            Knight color.
    '''
    def __init__(self, position: list, available_positions: list, COLOR: str) -> None:
        super().__init__(position, available_positions, COLOR)

    def get_available_positions(self, mode: bool=True) -> list:
        '''Get the available positions for the Knight to move to.

        Parameters
        ----------
        mode : :class:`bool`, optional
            Check if the available positions will be for the current player turn, by default True.

        Returns
        -------
        :class:`list`
            Available positions for the Knight to move to.
        '''
        # All the available positions for the Knight.
        all_available_positions = [
            [self.position[0]+2, self.position[1]+1], [self.position[0]-2, self.position[1]+1], # 2Right 1Up, 2Left 1Up.
            [self.position[0]+2, self.position[1]-1], [self.position[0]-2, self.position[1]-1], # 2Right 1Down, 2Left 1Down.
            [self.position[0]+1, self.position[1]+2], [self.position[0]+1, self.position[1]-2], # 2Up 1Right, 2Down 1Right.
            [self.position[0]-1, self.position[1]+2], [self.position[0]-1, self.position[1]-2], # 2Up 1Left, 2Down 1Left.
        ]
        available_positions = all_available_positions.copy() # Actual available positions.

        for i in all_available_positions:
            # Check if [the position is available on the board, there's no piece from the same color in this position].
            try:
                if (position_on_board := self.board[self.convert_to_letters(i)]) and position_on_board.COLOR == self.COLOR: # Check if there's a piece on this position with the same color.
                    available_positions.remove(i) # Remove the position.

            except IndexError: # Position not available on the board.
                available_positions.remove(i)

        return self.player.check_available_positions(self, available_positions) if mode else available_positions
