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
        """Get the available positions for the Rook to move to.

        Returns
        -------
        list[list[int]]
            Available positions for the Rook to move to.
        """
        available_positions = []
        directions = [0, 1, 2, 3]
        num = 1 # Number to add/sub from the piece position

        while directions:
            # Get all the direction for the Rook 
            positions = [
                [self.position[0]+num, self.position[1]], [self.position[0], self.position[1]+num], # Right, Up
                [self.position[0]-num, self.position[1]], [self.position[0], self.position[1]-num] # Left, Down
                ]

            for i in directions.copy():
                try:
                    # Check if [the position is available on the board, there's no piece from the same color in this position]
                    if (temp := self.board[self.convert_to_letters(positions[i])]):
                        directions.remove(i)

                        if temp.color == self.color:
                            continue

                    available_positions.append(positions[i])

                except IndexError:
                    directions.remove(i)

            num += 1

        return available_positions
