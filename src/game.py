import pygame

from const import *
from board import Board
from dragger import Dragger
from config import Config
from square import Square
from piece import *

class Game:
    
    def __init__(self):
        self.board = Board()

        self.dragger = Dragger()
        
        self.next_player = self.board.red
        self.hover_sqr = None


        self.config = Config()

        self.finish = False

    # blit methods

    def show_bg(self, surface):
        theme = self.config.theme

        for col in range(COLS):
            for row in range(ROWS):

                color = (49, 49, 49) if not Square.valid(col, row) else theme.color.light if (col + row) % 2 == 0 else theme.color.dark
                
                rect = (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

                pygame.draw.rect(surface, color, rect)
    
    def show_pieces(self, surface):
        theme = self.config.theme

        for col in range(COLS):
            for row in range(ROWS):

                if not self.board.squares[col][row].empty():
                    piece = self.board.squares[col][row].piece

                    # all pieces expect dragger piece
                    if piece is not self.dragger.piece:

                        texture_rect = piece.texture.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE / 2, row * SQUARE_SIZE + SQUARE_SIZE / 2))

                        surface.blit(piece.texture, texture_rect)
    
    def show_dragged_piece(self, surface):

        texture_rect = self.dragger.piece.texture.get_rect(center=(self.dragger.mouseX, self.dragger.mouseY))

        surface.blit(self.dragger.piece.texture, texture_rect)

    def show_moves(self, surface):

        if self.dragger.dragging:
            piece = self.dragger.piece
            
            for move in piece.moves + piece.captures:

                if move not in piece.checks:

                    circle = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)

                    if move.capture:
                        pygame.draw.circle(circle, (0, 0, 0, 40), (SQUARE_SIZE/2, SQUARE_SIZE/2), SQUARE_SIZE/2-SQUARE_SIZE*.02, 8)
                    else:
                        pygame.draw.circle(circle, (0, 0, 0, 30), (SQUARE_SIZE/2, SQUARE_SIZE/2), SQUARE_SIZE/7)

                    surface.blit(circle, (move.final.col * SQUARE_SIZE, move.final.row * SQUARE_SIZE))
    

    def next_turn(self):
        index = (self.board.players.index(self.next_player)+1) % 4
        self.next_player = self.board.players[index]
    
    def set_hover(self, col, row):
        self.hover_sqr = self.board.squares[col][row]
    
    def change_theme_color(self):
        self.config.change_theme_color()
    
    def change_theme_piece(self):
        theme = self.config.theme

        self.config.change_theme_piece()

        for col in range(COLS):
            for row in range(ROWS):
                
                if not self.board.squares[col][row].empty():
                    piece = self.board.squares[col][row].piece

                    piece.set_texture(theme.piece)

    def set_dead(self, player):

        theme = self.config.theme

        for col in range(COLS):
            for row in range(ROWS):
                
                if not self.board.squares[col][row].empty():
                    piece = self.board.squares[col][row].piece
                    
                    if piece.player == player:

                        piece.set_texture(theme.piece, True)

    def show_checks(self, surface):
        self.board.calc_valid_moves()

        for player in self.board.players:
            
            king = player.royal
            king.check = False

            for enemy in player.opponents:
                for piece in enemy.pieces:
                    for capture in piece.captures:
                        if capture.piece_class == King:
                            if capture.player == player:
                                king.check = True

            if king.check:

                color = (121, 0, 0) 
                
                rect = (king.col * SQUARE_SIZE, king.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

                pygame.draw.rect(surface, color, rect)

                
    
    def play_sound(self, captured=False):
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()
    
    def reset(self):
        self.__init__()

            



