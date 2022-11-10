import pygame as pg
import os
from const import *

class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.col = 0
        self.row = 0
        self.initial_col = 0
        self.initial_row = 0
    

    # other methods

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos
        self.col, self.row = self.mouseX // SQUARE_SIZE, self.mouseY // SQUARE_SIZE
    
    def save_initial(self):
        self.initial_col = self.col
        self.initial_row = self.row
    
    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True
    
    def undrag_piece(self):
        self.piece = None
        self.dragging = False