from src.master.piece import Piece


class Rook(Piece):
    '''Rook piece class.

        Parameters
        ----------
        position : :class:`list`
            Rook position on the board.
        available_positions : :class:`list`
            Available positions for the Rook to move to.
        COLOR : :class:`str`
            Rook color.
    '''
    def __init__(self, position: list, available_positions: list, COLOR: str) -> None:
        super().__init__(position, available_positions, COLOR)

    def get_available_position(self) -> list:
        '''Get the available positions for the Rook to move to.

        Returns
        -------
        :class:`list`
            Available positions for the Rook to move to.
        '''
        available_positions = []
        directions = [0, 1, 2, 3] # Index of the available positions.
        num = 1 # Number to add/sub to/from the piece position.

        while directions:
            # Get all the direction for the Rook.
            positions = [
                [self.position[0]+num, self.position[1]], [self.position[0], self.position[1]+num], # Right, Up.
                [self.position[0]-num, self.position[1]], [self.position[0], self.position[1]-num] # Left, Down.
            ]

            for i in directions.copy():
                # Check if [the position is available on the board, there's no piece from the same color in this position].
                try:
                    if (position_on_board := self.board[self.convert_to_letters(positions[i])]): # Check if there's a piece on this position.
                        directions.remove(i) # remove this direction.

                        if position_on_board.COLOR == self.COLOR:
                            continue

                    available_positions.append(positions[i]) # Add the position if it's not the same color.

                except IndexError: # Position is not available on the board.
                    directions.remove(i)

            num += 1

        return available_positions
