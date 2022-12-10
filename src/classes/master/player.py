from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.classes.master.piece import Piece
    from src.classes.pieces.king import King


class Player:
    '''Player class.

        Parameters
        ----------
        king : :class:`King`
            King piece of this player.
        pieces : :class:`list`[:class:`Piece`]
            All the player pieces.
        COLOR : :class:`str`
            Player color.
    '''
    players = {'white': None, 'black': None} # All players

    def __init__(self, king: King, pieces: list[Piece], COLOR: str) -> None:
        self.king = king
        self.pieces = pieces
        self.COLOR = COLOR
        self.players[self.COLOR] = self
        self.ENEMY_COLOR = 'black' if self.COLOR == 'white' else 'white'

    @staticmethod
    def all_available_positions(player: Player, mode: bool) -> list:
        '''Get all the Player's pieces available positions.

        Parameters
        ----------
        player : :class:`Player`
            Player to get his available positions.
        mode : :class:`bool`
            Check if the positions will be in nested list.

        Returns
        -------
        :class:`list`
            All available positions.
        '''
        all_positions = []

        for i in player.pieces:
            piece_available_positions = i.get_available_positions(False)
            all_positions.append(piece_available_positions) if mode else [all_positions.append(j) for j in piece_available_positions]

        return all_positions

    def check_available_positions(self, piece: Piece, all_available_positions: list) -> list:
        '''Get the available positions without having a checkmate.

        Parameters
        ----------
        piece : :class:`Piece`
            Piece to check for it.
        all_available_positions : :class:`list`
            All the available positions for the Piece.

        Returns
        -------
        :class:`list`
            Actual available positions for the Piece to move to.
        '''
        piece_current_position = piece.position
        available_positions = []

        for i in all_available_positions:
            piece.position = i

            if self.king.position not in self.all_available_positions(self.players[self.ENEMY_COLOR], False):
                available_positions.append(i)

        piece.position = piece_current_position
        return available_positions

    def check_checkmate(self) -> bool:
        '''Check if there's a checkmate.

        Returns
        -------
        :class:`bool`
            ``True`` if there's a checkmate, else ``False``.
        '''
        # Check if there's any enemy's piece can reach the "King".
        for i in self.players[self.ENEMY_COLOR].pieces:
            if self.king.position in i.available_positions:
                return True

        return False

    def check_lose(self) -> bool:
        '''Check if player lost.

        Returns
        -------
        :class:`bool`
            ``True`` if player lost, else ``False``.
        '''
        # Check if there's any available positions to move to, if not then the player lost.
        for i in self.pieces:
            if i.available_positions[0]:
                return False

        return True

    def check_piece(self, piece) -> bool:
        '''Check if the player has this piece.

        Parameters
        ----------
        piece : :class:`Piece`
            Piece to check.

        Returns
        -------
        :class:`bool`
            ``True`` if the piece exist, else ``False``.
        '''
        return True if piece in self.pieces else False

    def add_piece(self, piece) -> None:
        '''Add piece to the player's pieces.

        Parameters
        ----------
        piece : :class:`Piece`
            Piece to add.
        '''
        self.pieces.append(piece)

    def remove_piece(self, piece) -> None:
        '''Remove piece from the player's pieces.

        Parameters
        ----------
        piece : :class:`Piece`
            Piece to remove.
        '''
        self.pieces.remove(piece)
