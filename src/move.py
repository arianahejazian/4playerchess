class Move:

    def __init__(self, initial, final, en=False,capture=False,piece_class=None, player=None, double_move=False, castle = False):

        # initial and final squares
        self.initial = initial
        self.final = final
        self.capture = capture
        self.en = en
        self.piece_class = piece_class
        self.player = player
        self.double_move = double_move
        self.castle = castle
    
    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final