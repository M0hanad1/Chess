from src.master.piece import Piece


class Pawn(Piece):
    '''Pawn piece class.

        Parameters
        ----------
        position : :class:`list`
            Pawn position on the board.
        available_positions : :class:`list`
            Available positions for the Pawn to move to.
        color : :class:`str`
            Pawn color.
    '''
    def __init__(self, position: list, available_positions: list, color: str) -> None:
        super().__init__(position, available_positions, color)

    def check_move(self) -> bool:
        '''Check if the Pawn has moved from it first place.

        Returns
        -------
        :class:`bool`
            ``True`` if it moved, else ``False``.
        '''
        return True if self.position[1] != 1 else False

    def check_replace(self) -> bool:
        '''Check if the Pawn reach the end of the board.

        Returns
        -------
        :class:`bool`
            ``True`` if it reached the end, else ``False``.
        '''
        return True if self.position[1] == 7 else False

    def get_available_position(self) -> list:
        '''Get the available positions for the Pawn to move to.

        Returns
        -------
        :class:`list`
            Available positions for the Pawn to move to.
        '''

        # All the available positions for the Pawn.
        all_available_positions = [
            [self.position[0], self.position[1]+1], [self.position[0]+1, self.position[1]+1], # 1Up, 1Right 1Up.
            [self.position[0]-1, self.position[1]+1], [self.position[0], self.position[1]+2] # 1Left 1Up, 2Up.
        ]
        available_positions = all_available_positions.copy() # Actual available positions.

        for i in range(len(all_available_positions)):
            position = all_available_positions[i]

            # Check if [the position is available on the board, there's no piece from the same color in this position].
            try:
                if (position_on_board := self.board[self.convert_to_letters(position)]): # Check if there's a piece on this position.
                    if i not in [1, 2] or self.color == position_on_board.color: # Check if it's not moving to the right/left, or if it's the same color.
                        available_positions.remove(position) # remove this position.

                else: # if there's no piece in this position.
                    if i == 3 and (self.check_move() or all_available_positions[0] not in available_positions): # Check if it's moving forward twice, and check if [it's moved from it's first place, position not available in the board].
                        available_positions.remove(position)

            except IndexError: # Position not available in the board.
                available_positions.remove(position)

        return available_positions
