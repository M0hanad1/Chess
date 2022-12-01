from src.master.piece import Piece


class Pawn(Piece):
    """Pawn piece class.

        Parameters
        ----------
        position : list[int]
            Pawn position on the board.
        available_positions : list[list[int]]
            Available positions for the Pawn to move to.
        color : str
            Pawn color.
    """
    def __init__(self, position: list[int], available_positions: list[list[int]], color: str) -> None:
        super().__init__(position, available_positions, color)

    def check_move(self) -> bool:
        """Check if the Pawn has moved from it first place.

        Returns
        -------
        bool
            True if it moved, else false.
        """
        return True if self.position[1] != 1 else False

    def get_available_position(self) -> list[list[int]]:
        """Get the available positions for the Pawn to move to.

        Returns
        -------
        list[list[int]]
            Available positions for the Pawn to move to.
        """

        all_available_positions = [
            [self.position[0], self.position[1]+1], [self.position[0]+1, self.position[1]+1], # 1Up, 1Right 1Up.
            [self.position[0]-1, self.position[1]+1], [self.position[0], self.position[1]+2] # 1Left 1Up, 2Up.
        ]
        positions_result = all_available_positions.copy()

        for i in range(len(all_available_positions)):
            position = all_available_positions[i]

            # Check if [the position is available on the board, there's no piece from the same color in this position].
            try:
                if (position_on_board := self.board[self.convert_to_letters(position)]):
                    if i not in [1, 2] or self.color == position_on_board.color:
                        positions_result.remove(position)

                else:
                    if i == 3 and (self.check_move() or all_available_positions[0] not in positions_result):
                        positions_result.remove(position)

            except IndexError:
                positions_result.remove(position)

        return positions_result
