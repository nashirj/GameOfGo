class Go:
    def __init__(self, size):
        if size > 25:
            raise ValueError("Board cannot be larger than 25 by 25")
        self.height = size
        self.width = size
        self.board = [["." for i in range(self.height)] for j in range(self.width)]
        self.turn = "black"
        self.white_piece = 'o'
        self.black_piece = 'x'
        
        
    def set_position(self, pos):
        row = abs(ord(pos[0])-ord('0')-self.width)
        col = ord(pos[1])-ord('A')
        if row >= self.height or row < 0 or col >= self.width or col < 0:
            raise ValueError("Cannot place a stone with out of bounds coordinates")
        if self.board[row][col] != '.':
            raise ValueError("Cannot place a stone on an existing stone")
        self.board[row][col] = self.black_piece if self.turn == "black" else self.white_piece
        
        
    def move(self, *positions):
        '''
        row: pos[0]
        col: pos[1]
        '''
        for pos in positions:
            self.set_position(pos)
            self.end_turn()
            
        
    def get_position(self, pos):
        '''
        row: pos[0]
        col: pos[1]
        '''
        row = abs(ord(pos[0])-ord('0')-self.width)
        col = ord(pos[1])-ord('A')
        return self.board[row][col]
        
        
    def end_turn(self):
        if self.turn == "black":
            # do black turn
            self.turn = "white"
#             return "black"
        elif self.turn == "white":
            # do white turn
            self.turn = "black"
#             return "white"
        else:
            raise ValueError("Value of turn should not be modified outside of this method")
            