'''
Ariana Hejazian

https://github.com/arianahejazian

'''

import pygame
import sys

from const import *
from game import Game
from move import Move
from square import Square

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT))
        pygame.display.set_caption('4 Player Chess')
        pygame.display.set_icon(pygame.image.load('assets/images/icon.png'))
        self.game = Game()

    def main_loop(self):
        
        game = self.game
        screen = self.screen
        board = self.game.board
        dragger = self.game.dragger

        game.show_bg(screen)
        
        while True:
            game.show_bg(screen)
            if not game.finish: game.show_checks(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                #dragger.update_blit(screen, game.config.theme)
                game.show_dragged_piece(screen)

            for event in pygame.event.get():
                
                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    
                    if not game.finish:
                        
                        # check if square has a piece
                        if not board.squares[dragger.col][dragger.row].empty():
                            piece = board.squares[dragger.col][dragger.row].piece

                            if piece.player == game.next_player:
                                dragger.drag_piece(piece)
                                dragger.save_initial()
                                
                                board.calc_valid_moves()

                                
                                game.show_bg(screen)
                                game.show_checks(screen)
                                game.show_moves(screen)
                                game.show_pieces(screen)
                            

                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if not game.finish:
                        if dragger.dragging:
                            dragger.update_mouse(event.pos)
                            
                            game.show_bg(screen)
                            game.show_checks(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                            #dragger.update_blit(screen, game.config.theme)
                            game.show_dragged_piece(screen)

                # click release
                elif event.type == pygame.MOUSEBUTTONUP :
                    if not game.finish:

                        if dragger.dragging:
                            dragger.update_mouse(event.pos)

                            released_col = dragger.mouseX // SQUARE_SIZE
                            released_row = dragger.mouseY // SQUARE_SIZE
                            
                            initial = Square(dragger.initial_col, dragger.initial_row)
                            final = Square(released_col, released_row)

                            move = Move(initial, final)

                            for m in dragger.piece.moves + dragger.piece.captures:
                                if m == move:
                                    move = m
                                    break
                            
                            if (move in dragger.piece.moves + dragger.piece.captures) and (move not in dragger.piece.checks):

                                if move.capture:
                                    if move.en:
                                        if dragger.piece.player.idx == 0:
                                            p = board.squares[initial.col][initial.row-1].piece
                                            board.squares[initial.col][initial.row-1].piece = 0
                                            board.players[p.player.idx].pieces.remove(p)
                                        if dragger.piece.player.idx == 1:
                                            p = board.squares[initial.col+1][initial.row].piece
                                            board.squares[initial.col+1][initial.row].piece = 0
                                            board.players[p.player.idx].pieces.remove(p)
                                        if dragger.piece.player.idx == 2:
                                            p = board.squares[initial.col][initial.row+1].piece
                                            board.squares[initial.col][initial.row+1].piece = 0
                                            board.players[p.player.idx].pieces.remove(p)
                                        if dragger.piece.player.idx == 3:
                                            p = board.squares[initial.col-1][initial.row].piece
                                            board.squares[initial.col-1][initial.row].piece = 0
                                            board.players[p.player.idx].pieces.remove(p)
                                    else:
                                        p = board.squares[move.final.col][move.final.row].piece

                                        board.players[p.player.idx].pieces.remove(p)

                                if move.castle:
                                    board.castle(dragger.piece, move)

                                board.move(dragger.piece, move)
                                board.last_moves[dragger.piece.player.idx] = move
                                game.play_sound(m.capture)
                                
                                game.show_bg(screen)
                                game.show_checks(screen)
                                game.show_moves(screen)
                                game.show_pieces(screen)

                                game.next_turn()
                                
                                board.calc_valid_moves()
                                count = 0
                                for p in game.next_player.pieces:
                                    for m in p.moves + p.captures:
                                        if not m in p.checks:
                                            count += 1
                                
                                if count == 0:
                                    game.finish = True
                                    
                                    game.set_dead(game.next_player)



                        dragger.undrag_piece()
                
                # key press
                elif event.type == pygame.KEYDOWN:
                    if not game.finish:
                        if event.key == pygame.K_q:
                            game.change_theme_color()

                    if not game.finish:
                        if event.key == pygame.K_w:
                            game.change_theme_piece()
                    
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger

                # exit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

main = Main()
main.main_loop()