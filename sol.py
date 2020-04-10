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
        
        
    def get_coordinates(self, pos):
        row = abs(ord(pos[0])-ord('0')-self.width)
        col = ord(pos[1])-ord('A')
        return row, col
        
    def coordinates_to_pos(self, row, col):
        row_ch = chr(abs(row-self.width)+ord('0'))
        col_ch = chr(col+ord('A'))
        return "{}{}".format(row_ch, col_ch)
        
    def set_position(self, pos):
        row, col = self.get_coordinates(pos)
        if row >= self.height or row < 0 or col >= self.width or col < 0:
            raise ValueError("Cannot place a stone with out of bounds coordinates")
        if self.board[row][col] != '.':
            raise ValueError("Cannot place a stone on an existing stone")
        self.board[row][col] = self.black_piece if self.turn == "black" else self.white_piece
        
        
    def has_liberties(self, pos):
        row, col = self.get_coordinates(pos)
        if row > 0:
            if self.board[row-1][col] == '.':
                return True
        if row < self.height-1:
            if self.board[row+1][col] == '.':
                return True
        if col > 0:
            if self.board[row][col-1] == '.':
                return True
        if col < self.height-1:
            if self.board[row][col+1] == '.':
                return True
        return False
        
    
    def get_neighbors(self, pos):
        row, col = self.get_coordinates(pos)
        neighbors = []
        if row > 0:
            neighbors.append(self.coordinates_to_pos(row-1,col))
        if row < self.height-1:
            neighbors.append(self.coordinates_to_pos(row+1,col))
        if col > 0:
            neighbors.append(self.coordinates_to_pos(row,col-1))
        if col < self.height-1:
            neighbors.append(self.coordinates_to_pos(row,col+1))
        return neighbors
    
    
    def remove_stones(self, pos, stones_to_remove):
        row, col = self.get_coordinates(pos)
        self.board[row][col] = '.'
        # remove neighbors if they are same stone type
        neighbors = self.get_neighbors(pos)
        while neighbors:
            for neighbor in neighbors:
                n_row, n_col = self.get_coordinates(neighbor)
                if self.board[n_row][n_col] == stones_to_remove:
                    self.remove_stones(neighbor, stones_to_remove)
                self.board[n_row][n_col] = '.'
                neighbors.remove(neighbor)
    
    def move(self, *positions):
        '''
        row: pos[0]
        col: pos[1]
        '''
        for pos in positions:
            print(pos)
            self.set_position(pos)
            for neighbor in self.get_neighbors(pos):
                if not self.has_liberties(neighbor):
                    stones_to_remove = self.black_piece if self.turn == "white" else self.white_piece
                    self.remove_stones(neighbor, stones_to_remove)
            self.end_turn()
            
            
    def get_position(self, pos):
        '''
        row: pos[0]
        col: pos[1]
        '''
        row, col = self.get_coordinates(pos)
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
            