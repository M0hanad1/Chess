from src.master.piece import Piece


class Knight(Piece):
    def __init__(self, position: list[int], positions_to_move: list[list], color: str):
        super().__init__(position, positions_to_move, color)

    def get_available_position(self):
        self.check_available_positions([
            [self.position[0]+2, self.position[1]+1], [self.position[0]-2, self.position[1]+1],
            [self.position[0]+2, self.position[1]-1], [self.position[0]-2, self.position[1]-1],
            [self.position[0]+1, self.position[1]+2], [self.position[0]+1, self.position[1]-2],
            [self.position[0]-1, self.position[1]+2], [self.position[0]-1, self.position[1]-2],
        ])