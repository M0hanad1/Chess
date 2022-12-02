from src.master.piece import Piece


class Bishop(Piece):
    """Bishop piece class.

        Parameters
        ----------
        position : list[int]
            Bishop position on the board.
        available_positions : list[list[int]]
            Available positions for the Bishop to move to.
        color : str
            Bishop color.
    """
    def __init__(self, position: list[int], available_positions: list[list[int]], color: str) -> None:
        super().__init__(position, available_positions, color)

    def get_available_position(self) -> list[list[int]]:
        """Get the available positions for the Bishop to move to.

        Returns
        -------
        list[list[int]]
            Available positions for the Bishop to move to.
        """
        available_positions = []
        directions = [0, 1, 2, 3] # Index of the available positions.
        num = 1 # Number to add/sub from the piece position.

        while directions:
            # Get all the direction for the Rook.
            positions = [
                [self.position[0]+num, self.position[1]+num], [self.position[0]+num, self.position[1]-num], # Right Up, Right Down.
                [self.position[0]-num, self.position[1]+num], [self.position[0]-num, self.position[1]-num] # Left Up, Left Down.
                ]

            for i in directions.copy():
                # Check if [the position is available on the board, there's no piece from the same color in this position].
                try:
                    if (position_on_board := self.board[self.convert_to_letters(positions[i])]): # Check if there's a piece on this position.
                        directions.remove(i) # remove this direction.

                        if position_on_board.color == self.color:
                            continue

                    available_positions.append(positions[i]) # Add the position if it's not the same color.

                except IndexError: # Position is not available on the board.
                    directions.remove(i)

            num += 1

        return available_positions