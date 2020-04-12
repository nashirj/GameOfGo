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
        self.stones_to_remove = self.white_piece
        
        
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


    def get_val_at_pos(self, pos):
        row, col = self.get_coordinates(pos)
        return self.board[row][col]


    def get_stone_group(self, pos, stone_type):
        stone_group = []
        visited = []
        self.get_stone_group_helper(pos, stone_type, visited, stone_group)
        return stone_group


    def get_stone_group_helper(self, pos, stone_type, visited, stone_group):
        row, col = self.get_coordinates(pos)
        if self.board[row][col] != stone_type:
            return stone_group
        visited.append(pos)
        stone_group.append(pos)
        neighbors = self.get_neighbors(pos)
        for stone in neighbors:
            if stone in visited:
                continue
            s_row, s_col = self.get_coordinates(stone)
            if self.board[s_row][s_col] == stone_type:
                self.get_stone_group_helper(stone, stone_type, visited, stone_group)
        return stone_group


    # need to check if a given stone group has liberties. if not, remove it
    def has_liberties(self, pos):
        row, col = self.get_coordinates(pos)
        stone_type = self.board[row][col]
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


    def get_neighbors(self, pos, stone_type=None):
        row, col = self.get_coordinates(pos)
        neighbors = []
        if row > 0:
            # short circuit if no stone type passed, else check for stone_type before adding
            if not stone_type or self.board[row-1][col] == stone_type:
                neighbors.append(self.coordinates_to_pos(row-1,col))
        if row < self.height-1:
            if not stone_type or self.board[row+1][col] == stone_type:
                neighbors.append(self.coordinates_to_pos(row+1,col))
        if col > 0:
            if not stone_type or self.board[row][col-1] == stone_type:
                neighbors.append(self.coordinates_to_pos(row,col-1))
        if col < self.height-1:
            if not stone_type or self.board[row][col+1] == stone_type:
                neighbors.append(self.coordinates_to_pos(row,col+1))
        return neighbors


    def remove_stones(self, *stones_to_remove):
        for stone in stones_to_remove:
            if self.get_val_at_pos(stone) == self.stones_to_remove:
                stone_group = self.get_stone_group(stone, self.stones_to_remove)
                if all(not self.has_liberties(stone) for stone in stone_group):
                    for remove in stone_group:
                        row, col = self.get_coordinates(remove)
                        self.board[row][col] = '.'


    def move(self, *positions):
        for pos in positions:
            self.set_position(pos)
            enemy_neighbors = self.get_neighbors(pos, self.stones_to_remove)
            if enemy_neighbors:
                self.remove_stones(*enemy_neighbors)
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
            self.turn = "white"
            self.stones_to_remove = self.black_piece
        elif self.turn == "white":
            # do white turn
            self.turn = "black"
            self.stones_to_remove = self.white_piece
        else:
            raise ValueError("Value of turn should not be modified outside of this method")


    # public means of ending/passing turn
    def pass_turn(self):
        self.end_turn()


    # TODO: implement this, need to keep track of game state
    def rollback(self, num_turns):
        pass


    def print_board(self):
        print(" ", end="")
        for i in range(self.width):
            print(" {}".format(chr(ord('A')+i)),end="")
        print("")
        height = self.height
        for row in self.board:
            print("{}".format(height), end="")
            height -= 1
            for cell in row:
                print(" {}".format(cell), end="")
            print("")


    def reset_board(self):
        self.turn = black
        self.board = [["." for i in range(self.height)] for j in range(self.width)]
