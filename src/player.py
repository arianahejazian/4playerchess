class Player:

    def __init__(self, color, idx, royal=None):

        self.color = color
        self.idx = idx
        self.pieces = []
        self.teammate = None
        self.opponents = None
        self.royal = royal