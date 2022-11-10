import os
import pygame as pg
from const import *

class Piece:

    def __init__(self, name, player, value, col=None, row=None):
        self.name = name
        self.player = player
        self.value = value

        self.texture = None
        self.set_texture('standard')

        self.moves = []
        self.captures = []
        self.checks = []

        self.moved = False
        self.col = col
        self.row = row
        self.player.pieces.append(self)
        if isinstance(self, King):
            self.player.royal = self
    
    def set_texture(self, theme, dead=False):
        if not dead:
            self.texture = os.path.join(f'assets/images/pieces/{theme}/{self.player.color}/{self.name}.png')
            self.texture = pg.image.load(self.texture)
            self.texture = pg.transform.smoothscale(self.texture, (SQUARE_SIZE, SQUARE_SIZE))
        else:
            self.texture = os.path.join(f'assets/images/pieces/{theme}/dead/{self.name}.png')
            self.texture = pg.image.load(self.texture)
            self.texture = pg.transform.smoothscale(self.texture, (SQUARE_SIZE, SQUARE_SIZE))

class Pawn(Piece):

    def __init__(self, player):
        super().__init__('pawn', player, 1.0)
        self.moved = False
        self.en_passant = True
        self.loop = False
        self.steps = {
                'red': [Step(0, -1), Step(0, -2), Step(-1, -1), Step(+1, -1)],
                'blue': [Step(+1, 0), Step(+2, 0), Step(+1, +1), Step(+1, -1)],
                'yellow': [Step(0, +1), Step(0, +2), Step(-1, +1), Step(+1, +1)],
                'green': [Step(-1, 0), Step(-2, 0), Step(-1, +1), Step(-1, -1)],
            }
    
    @staticmethod
    def steps():
        return {
                'red': [Step(0, -1), Step(0, -2), Step(-1, -1), Step(+1, -1)],
                'blue': [Step(+1, 0), Step(+2, 0), Step(+1, +1), Step(+1, -1)],
                'yellow': [Step(0, +1), Step(0, +2), Step(-1, +1), Step(+1, +1)],
                'green': [Step(-1, 0), Step(-2, 0), Step(-1, +1), Step(-1, -1)],
            }

class Knight(Piece):

    def __init__(self, player):
        super().__init__('knight', player, 3.0)
        self.loop = False
        self.steps = [
                Step(-1, +2),
                Step(+1, +2),
                Step(-2, +1),
                Step(+2, +1),
                Step(-2, -1),
                Step(+2, -1),
                Step(-1, -2),
                Step(+1, -2),
            ]

    @staticmethod
    def steps():
        return [
                Step(-1, +2),
                Step(+1, +2),
                Step(-2, +1),
                Step(+2, +1),
                Step(-2, -1),
                Step(+2, -1),
                Step(-1, -2),
                Step(+1, -2),
            ]

class Bishop(Piece):

    def __init__(self, player):
        super().__init__('bishop', player, 4.0)
        self.loop = True
        self.steps = [
                Step(-1, -1),
                Step(+1, +1),
                Step(-1, +1),
                Step(+1, -1)
            ]
    
    @staticmethod
    def steps():
        return [
                Step(-1, -1),
                Step(+1, +1),
                Step(-1, +1),
                Step(+1, -1)
            ]

class Rook(Piece):

    def __init__(self, player):
        super().__init__('rook', player, 5.0)
        self.moved = False
        self.loop = True
        self.steps = [
                Step(-1, 0),
                Step(+1, 0),
                Step(0, +1),
                Step(0, -1)
            ]

    @staticmethod
    def steps():
        return [
                Step(-1, 0),
                Step(+1, 0),
                Step(0, +1),
                Step(0, -1)
            ]

class Queen(Piece):

    def __init__(self, player):
        super().__init__('queen', player, 9.0)
        self.loop = True
        self.steps = [
                Step(-1, -1),
                Step(+1, +1),
                Step(-1, +1),
                Step(+1, -1),
                Step(-1, 0),
                Step(+1, 0),
                Step(0, +1),
                Step(0, -1)
            ]
    
    @staticmethod
    def steps():
        return [
                Step(-1, -1),
                Step(+1, +1),
                Step(-1, +1),
                Step(+1, -1),
                Step(-1, 0),
                Step(+1, 0),
                Step(0, +1),
                Step(0, -1)
            ]

class King(Piece):

    def __init__(self, player):
        super().__init__('king', player, 10000.0)
        self.moved = False
        self.loop = False
        self.check = False
        self.steps = [
                Step(-1, -1),
                Step(+1, +1),
                Step(-1, +1),
                Step(+1, -1),
                Step(-1, 0),
                Step(+1, 0),
                Step(0, +1),
                Step(0, -1)
            ]
    
    @staticmethod
    def steps():
        return [
                Step(-1, -1),
                Step(+1, +1),
                Step(-1, +1),
                Step(+1, -1),
                Step(-1, 0),
                Step(+1, 0),
                Step(0, +1),
                Step(0, -1)
            ]

class Step:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y


steps = {
    'pawn': {
        'red': [Step(0, -1), Step(0, -2), Step(-1, -1), Step(+1, -1)],
        'blue': [Step(+1, 0), Step(+2, 0), Step(+1, +1), Step(+1, -1)],
        'yellow': [Step(0, +1), Step(0, +2), Step(-1, +1), Step(+1, +1)],
        'green': [Step(-1, 0), Step(-2, 0), Step(-1, +1), Step(-1, -1)],
    },
    'knight': [
        Step(-1, +2),
        Step(+1, +2),
        Step(-2, +1),
        Step(+2, +1),
        Step(-2, -1),
        Step(+2, -1),
        Step(-1, -2),
        Step(+1, -2),
    ],
    'bishop': [
        Step(-1, -1),
        Step(+1, +1),
        Step(-1, +1),
        Step(+1, -1)
    ],
    'rook': [
        Step(-1, 0),
        Step(+1, 0),
        Step(0, +1),
        Step(0, -1)
    ],
    'queen': [
        Step(-1, -1),
        Step(+1, +1),
        Step(-1, +1),
        Step(+1, -1),
        Step(-1, 0),
        Step(+1, 0),
        Step(0, +1),
        Step(0, -1)
    ],
    'king': [
        Step(-1, -1),
        Step(+1, +1),
        Step(-1, +1),
        Step(+1, -1),
        Step(-1, 0),
        Step(+1, 0),
        Step(0, +1),
        Step(0, -1)
    ]
}

loop = {
    Pawn: False,
    Knight: False,
    Bishop: True,
    Rook: True,
    Queen: True,
    King: False
}