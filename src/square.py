from const import *
from piece import Piece

class Square:

    def __init__(self, col, row, piece=None):

        self.col = col
        self.row = row
        self.piece = piece


    def empty(self):
        return not isinstance(self.piece, Piece)

    def enemy(self, player):
        return True if self.piece.player in player.opponents else False

    @staticmethod
    def valid(col, row):
        if (col<0 or col >13 or row<0 or row >13): return False
        return False if (col <= 2 or col >= 11) and (row <= 2 or row >= 11) else True
    
    def __eq__(self, other):
        return self.col == other.col and self.row == other.row