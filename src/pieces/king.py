from src.master.piece import Piece


class King(Piece):
    '''King piece class.

        Parameters
        ----------
        position : :class:`list`
            King position on the board.
        available_positions : :class:`list`
            Available positions for the King to move to.
        color : :class:`str`
            King color.
    '''
    def __init__(self, position: list, available_positions: list, color: str) -> None:
        super().__init__(position, available_positions, color)

    def get_available_position(self) -> list:
        '''Get the available positions for the King to move to.

        Returns
        -------
        :class:`list`
            Available positions for the King to move to.
        '''

        # All the available positions for the King.
        all_available_positions = [
            [self.position[0]+1, self.position[1]], [self.position[0], self.position[1]+1], # Right, Up.
            [self.position[0]-1, self.position[1]], [self.position[0], self.position[1]-1], # Left, Down.
            [self.position[0]+1, self.position[1]+1], [self.position[0]+1, self.position[1]-1], # Right Up, Right Down.
            [self.position[0]-1, self.position[1]+1], [self.position[0]-1, self.position[1]-1] # Left Up, Left Down.
        ]
        available_positions = all_available_positions.copy() # Actual available positions.

        for i in all_available_positions:
            # Check if [the position is available on the board, there's no piece from the same color in this position].
            try:
                if (position_on_board := self.board[self.convert_to_letters(i)]) and position_on_board.color == self.color: # Check if there's a piece on this position with the same color.
                    available_positions.remove(i) # Remove the position.

            except IndexError: # Position not available on the board.
                available_positions.remove(i)

        return available_positions
