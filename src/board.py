from const import *
from square import Square
from piece import *
from move import Move
from player import Player

class Board:

    def __init__(self):
        self.squares = [[Square(col, row) for row in range(ROWS)] for col in range(COLS)]
        self.mode = 'team'

        self.red = Player('red', 0)
        self.blue = Player('blue', 1)
        self.yellow = Player('yellow', 2)
        self.green = Player('green', 3)
        self.players = [self.red, self.blue, self.yellow, self.green]
        self.set_teamamtes()
        self.fill_board()
        
        self.last_moves = [None, None, None, None]

    def set_teamamtes(self):

        if self.mode == 'team':
            self.red.teammate = [self.red, self.yellow]
            self.blue.teammate = [self.blue, self.green]
            self.yellow.teammate = [self.red, self.yellow]
            self.green.teammate = [self.blue, self.green]

            self.red.opponents = [self.blue, self.green]
            self.blue.opponents = [self.red, self.yellow]
            self.yellow.opponents = [self.blue, self.green]
            self.green.opponents = [self.red, self.yellow]

    
    def fill_board(self):

        position = [[0,0,0,Rook(self.blue),Knight(self.blue),Bishop(self.blue),King(self.blue),Queen(self.blue),Bishop(self.blue),Knight(self.blue),Rook(self.blue),0,0,0],
                    [0,0,0,Pawn(self.blue),Pawn(self.blue),Pawn(self.blue),Pawn(self.blue),Pawn(self.blue),Pawn(self.blue),Pawn(self.blue),Pawn(self.blue),0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [Rook(self.yellow),Pawn(self.yellow),0,0,0,0,0,0,0,0,0,0,Pawn(self.red),Rook(self.red)],
                    [Knight(self.yellow),Pawn(self.yellow),0,0,0,0,0,0,0,0,0,0,Pawn(self.red),Knight(self.red)],
                    [Bishop(self.yellow),Pawn(self.yellow),0,0,0,0,0,0,0,0,0,0,Pawn(self.red),Bishop(self.red)],
                    [King(self.yellow),Pawn(self.yellow),0,0,0,0,0,0,0,0,0,0,Pawn(self.red),Queen(self.red)],
                    [Queen(self.yellow),Pawn(self.yellow),0,0,0,0,0,0,0,0,0,0,Pawn(self.red),King(self.red)],
                    [Bishop(self.yellow),Pawn(self.yellow),0,0,0,0,0,0,0,0,0,0,Pawn(self.red),Bishop(self.red)],
                    [Knight(self.yellow),Pawn(self.yellow),0,0,0,0,0,0,0,0,0,0,Pawn(self.red),Knight(self.red)],
                    [Rook(self.yellow),Pawn(self.yellow),0,0,0,0,0,0,0,0,0,0,Pawn(self.red),Rook(self.red)],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,Pawn(self.green),Pawn(self.green),Pawn(self.green),Pawn(self.green),Pawn(self.green),Pawn(self.green),Pawn(self.green),Pawn(self.green),0,0,0],
                    [0,0,0,Rook(self.green),Knight(self.green),Bishop(self.green),Queen(self.green),King(self.green),Bishop(self.green),Knight(self.green),Rook(self.green),0,0,0]]
        
        for col in range(COLS):
            for row in range(ROWS):
                self.squares[col][row].piece = position[col][row]
                if isinstance(position[col][row], Piece):
                    self.squares[col][row].piece.col = col
                    self.squares[col][row].piece.row = row           


    def move(self, piece, move):
        
        self.squares[move.initial.col][move.initial.row].piece = 0
        self.squares[move.final.col][move.final.row].piece = piece

        piece.col = move.final.col
        piece.row = move.final.row

    def check_promotion(self, piece, move):

        if piece.player == 'red' and move.final.row == 13 - self.promotion:
            self.squares[move.final.col][move.final.row].piece = Queen(piece.player)
        if piece.player == 'blue' and move.final.col == self.promotion:
            self.squares[move.final.col][move.final.row].piece = Queen(piece.player)
        if piece.player == 'yellow' and move.final.row == self.promotion:
            self.squares[move.final.col][move.final.row].piece = Queen(piece.player)
        if piece.player == 'green' and move.final.col == 13 - self.promotion:
            self.squares[move.final.col][move.final.row].piece = Queen(piece.player)

    def castle(self, piece, move):
        if piece.player.idx == 0:
            if move.final.col == 9:
                self.squares[8][13].piece = self.squares[10][13].piece
                self.squares[10][13].piece = 0
                self.squares[8][13].piece.col = 8
                self.squares[8][13].piece.row = 13

            elif move.final.col == 5:
                self.squares[6][13].piece = self.squares[3][13].piece
                self.squares[3][13].piece = 0
                self.squares[6][13].piece.col = 6
                self.squares[6][13].piece.row = 13
        
        if piece.player.idx == 1:
            if move.final.row == 4:
                self.squares[0][5].piece = self.squares[0][3].piece
                self.squares[0][3].piece = 0
                self.squares[0][5].piece.col = 0
                self.squares[0][5].piece.row = 5

            elif move.final.row == 8:
                self.squares[0][7].piece = self.squares[0][10].piece
                self.squares[0][10].piece = 0
                self.squares[0][7].piece.col = 0
                self.squares[0][7].piece.row = 7
        
        if piece.player.idx == 2:
            if move.final.col == 4:
                self.squares[5][0].piece = self.squares[3][0].piece
                self.squares[3][0].piece = 0
                self.squares[5][0].piece.col = 5
                self.squares[5][0].piece.row = 0

            elif move.final.col == 8:
                self.squares[7][0].piece = self.squares[10][0].piece
                self.squares[10][0].piece = 0
                self.squares[7][0].piece.col = 7
                self.squares[7][0].piece.row = 0

        if piece.player.idx == 3:
            if move.final.row == 9:
                self.squares[13][8].piece = self.squares[13][10].piece
                self.squares[13][10].piece = 0

            elif move.final.row == 5:
                self.squares[13][6].piece = self.squares[13][3].piece
                self.squares[13][3].piece = 0

    def calc_castle(self, player):

        if player.idx == 0: 
            idx = [
                {'rook': (10, 13), 'squares': [(8, 13), (9, 13)], 'checks': [(7, 13), (8, 13), (9, 13)], 'final': (9, 13)},
                {'rook': (3, 13), 'squares': [(4, 13), (5, 13), (6, 13)], 'checks': [(5, 13), (6, 13), (7, 13)], 'final': (5, 13)},
                ]
            initial = self.squares[7][13]
        elif player.idx == 1: 
            idx = [
                {'rook': (0, 3), 'squares': [(0, 4), (0, 5)], 'checks': [(0, 4), (0, 5), (0, 6)], 'final': (0, 4)},
                {'rook': (0, 10), 'squares': [(0, 7), (0, 8), (0, 9)], 'checks': [(0, 6), (0, 7), (0, 8)], 'final': (0, 8)},
                ]
            initial = self.squares[0][6]
        elif player.idx == 2: 
            idx = [
                {'rook': (3, 0), 'squares': [(4, 0), (5, 0)], 'checks': [(4, 0), (5, 0), (6, 0)], 'final': (4, 0)},
                {'rook': (10, 0), 'squares': [(7, 0), (8, 0), (9, 0)], 'checks': [(6, 0), (7, 0), (8, 0)], 'final': (8, 0)},
                ]
            initial = self.squares[6][0]
        elif player.idx == 3: 
            idx = [
                {'rook': (13, 10), 'squares': [(13, 8), (13, 9)], 'checks': [(13, 7), (13, 8), (13, 9)], 'final': (13, 9)},
                {'rook': (13, 3), 'squares': [(13, 4), (13, 5), (13, 6)], 'checks': [(13, 5), (13, 6), (13, 7)], 'final': (13, 5)},
                ]
            initial = self.squares[13][7]
        
        if not player.royal.moved:
            for i in idx:
                
                piece = self.squares[i['rook'][0]][i['rook'][1]].piece
                
                if piece.__class__ == Rook:
                    
                    if not piece.moved:
                        valid = True
                        for s in i['squares']:

                            if not self.squares[s[0]][s[1]].empty():
                                valid = False
                        
                        for c in i['checks']:

                            if self.square_is_attacked(player, c[0], c[1]):
                                valid = False

                        final = self.squares[i['final'][0]][i['final'][1]]
                        if valid: player.royal.moves.append(Move(initial, final, castle=True))                

        
    def calc_valid_moves(self):

        for player in self.players:
            for piece in player.pieces:
                piece.moves, piece.captures = self.calc_possible_moves(piece.__class__, player, piece.col, piece.row)
                piece.checks = []

        for player in self.players:
            for piece in player.pieces:
                for move in piece.moves + piece.captures:

                    temp_piece = self.squares[move.final.col][move.final.row].piece
                    
                    self.squares[move.initial.col][move.initial.row].piece = 0
                    self.squares[move.final.col][move.final.row].piece = piece

                    piece.col = move.final.col
                    piece.row = move.final.row

                    if self.square_is_attacked(player, player.royal.col, player.royal.row):
                        piece.checks.append(move)

                    self.squares[move.initial.col][move.initial.row].piece = piece
                    self.squares[move.final.col][move.final.row].piece = temp_piece

                    piece.col = move.initial.col
                    piece.row = move.initial.row
            
        for player in self.players:
            self.calc_castle(player)

    def square_is_attacked(self, player, col, row):

        # diagonal check
        for capture in self.calc_possible_moves(Bishop, player, col, row)[1]:

            # check by pawn
            if (capture.piece_class == Pawn):
                if capture.player.idx == 0:
                    if capture.final.row - row == 1:
                        return True
                elif capture.player.idx == 1:
                    if capture.final.col - col == -1:
                        return True
                elif capture.player.idx == 2:
                    if capture.final.row - row == -1:
                        return True
                elif capture.player.idx == 3:
                    if capture.final.col - col == 1:
                        return True
            
            # check by king
            elif (capture.piece_class == King):
                if ((capture.final.row - row == +1) or 
                    (capture.final.row - row == -1) or
                    (capture.final.col - col == +1) or
                    (capture.final.col - col == -1)):
                    return True
            
            # check by bishop or queen
            if (capture.piece_class == Bishop) or (capture.piece_class == Queen):
                return True
        
        # straight check
        for capture in self.calc_possible_moves(Rook, player, col, row)[1]:

            # check by king
            if (capture.piece_class == King):
                if ((capture.final.row - row == +1) or 
                    (capture.final.row - row == -1) or
                    (capture.final.col - col == +1) or
                    (capture.final.col - col == -1)):
                    return True
            
            # check by rook or queen
            elif (capture.piece_class == Rook) or (capture.piece_class == Queen):
                return True
        
        # L move check
        for capture in self.calc_possible_moves(Knight, player, col, row)[1]:
            
            # check by knight
            if (capture.piece_class == Knight):
                return True
        
        return False
                     

    def calc_possible_moves(self, piece, player, piece_col, piece_row):

        moves = []
        captures = []
        
        initial = self.squares[piece_col][piece_row]
        
        if piece != Pawn:
            
            for step in piece.steps():
                
                col = piece_col
                row = piece_row
                while True:
                    
                    col += step.X
                    row += step.Y
                    if Square.valid(col, row):
                        
                        final = self.squares[col][row]
                        if not final.empty():

                            if final.enemy(player): captures.append(Move(initial, final, False, True, final.piece.__class__, final.piece.player))

                            break
                        
                        moves.append(Move(initial, final))

                        if not loop[piece]: break
                    
                    else: break

        else:

            valid_steps = piece.steps()[player.color]
            
            final = self.squares[piece_col+valid_steps[0].X][piece_row+valid_steps[0].Y]
            if final.empty():
                
                moves.append(Move(initial, final))

                final = self.squares[piece_col+valid_steps[1].X][piece_row+valid_steps[1].Y]
                if final.empty():
                    if ((player.idx == 0 and piece_row == 12) or
                        (player.idx == 1 and piece_col == 1) or
                        (player.idx == 2 and piece_row == 1) or
                        (player.idx == 3 and piece_col == 12)):
                        moves.append(Move(initial, final, double_move=True))
        
            else:
                if final.enemy(player):
                    if final.piece.name == 'pawn':
                        if self.last_moves[final.piece.player.idx].final == final:
                            if self.last_moves[final.piece.player.idx].double_move:
                                
                                if final.piece.player.idx == 0 or final.piece.player.idx == 1:
                                    final = self.squares[piece_col+valid_steps[2].X][piece_row+valid_steps[2].Y]

                                elif final.piece.player.idx == 2 or final.piece.player.idx == 3:
                                    final = self.squares[piece_col+valid_steps[3].X][piece_row+valid_steps[3].Y]
                                
                                captures.append(Move(initial, final, True, True))



            for i in (2, 3):
                final = self.squares[piece_col+valid_steps[i].X][piece_row+valid_steps[i].Y]
                if not final.empty():
                    if final.enemy(player):
                        captures.append(Move(initial, final, False, True,  final.piece.__class__, final.piece.player))
            
        return moves, captures
