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

    def __init__(self, king, pieces: list, COLOR: str) -> None:
        self.king = king
        self.pieces = pieces
        self.COLOR = COLOR
        self.ENEMY_COLOR = 'black' if self.COLOR == 'white' else 'black'

        Player.players[self.COLOR] == self

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
