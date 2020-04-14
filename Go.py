class Go:
    def __init__(self, height, width=None):
        if height > 25:
            raise ValueError("Board cannot be larger than 25 by 25")
        if not width:
            width = height
        self.size = {"height":height, "width":width}
        self.board = [["." for i in range(self.size["width"])] for j in range(self.size["height"])]
        self.turn = "black"
        self.white_piece = 'o'
        self.black_piece = 'x'
        self.stones_to_remove = self.white_piece
        self.curr_stone_type = self.black_piece
        # for rollback
        self.game_states = [[row[:] for row in self.board]]
        self.handicap_stones_set = False


    def get_coordinates(self, pos):
        row = abs(int(pos[0:-1])-self.size["height"])
        col = ord(pos[-1])-ord('A')
        # go boards skip the letter 'I'
        if col >= 9:
            col -= 1
        if row >= self.size["height"] or row < 0:
            raise ValueError("Cannot place a stone in row {} for board of height {}".format(row, self.size["height"]))
        if col >= self.size["width"] or col < 0:
            raise ValueError("Cannot place a stone in col {} for board of width {}".format(col, self.size["width"]))
        return row, col


    def coordinates_to_pos(self, row, col):
        row_str = str(abs(row-self.size["height"]))
        # go boards skip the letter 'I'
        if col >= 9:
            col += 1
        col_ch = chr(col+ord('A'))
        return "{}{}".format(row_str, col_ch)


    def set_position(self, pos, reset=False):
        row, col = self.get_coordinates(pos)
        if row >= self.size["height"] or col >= self.size["width"]:
            raise ValueError("Cannot place a stone with out of bounds coordinates")
        if not reset and self.board[row][col] != '.':
            raise ValueError("Cannot place a stone on an existing stone")
        self.board[row][col] = '.' if reset else self.curr_stone_type


    def get_val_at_pos(self, pos):
        row, col = self.get_coordinates(pos)
        return self.board[row][col]


    def get_neighbors(self, pos, stone_type=None):
        row, col = self.get_coordinates(pos)
        neighbors = []
        if row > 0:
            # short circuit if no stone type passed, else check for stone_type before adding
            if not stone_type or self.board[row-1][col] == stone_type:
                neighbors.append(self.coordinates_to_pos(row-1,col))
        if row < self.size["height"]-1:
            if not stone_type or self.board[row+1][col] == stone_type:
                neighbors.append(self.coordinates_to_pos(row+1,col))
        if col > 0:
            if not stone_type or self.board[row][col-1] == stone_type:
                neighbors.append(self.coordinates_to_pos(row,col-1))
        if col < self.size["width"]-1:
            if not stone_type or self.board[row][col+1] == stone_type:
                neighbors.append(self.coordinates_to_pos(row,col+1))
        return neighbors


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


    def has_liberties(self, pos):
        row, col = self.get_coordinates(pos)
        stone_type = self.board[row][col]
        if row > 0:
            if self.board[row-1][col] == '.':
                return True
        if row < self.size["height"]-1:
            if self.board[row+1][col] == '.':
                return True
        if col > 0:
            if self.board[row][col-1] == '.':
                return True
        if col < self.size["width"]-1:
            if self.board[row][col+1] == '.':
                return True
        return False


    def remove_stones(self, *stones_to_remove):
        for stone in stones_to_remove:
            if self.get_val_at_pos(stone) == self.stones_to_remove:
                stone_group = self.get_stone_group(stone, self.stones_to_remove)
                if all(not self.has_liberties(stone) for stone in stone_group):
                    for remove in stone_group:
                        row, col = self.get_coordinates(remove)
                        self.board[row][col] = '.'


    def rollback(self, num_turns, illegal_ko=False):
        while len(self.game_states) > 1 and num_turns > 0:
            self.game_states.pop()
            self.board = [row[:] for row in self.game_states[-1]]
            # don't switch stone type or stones to remove if rollingback due to illegal ko
            if not illegal_ko:
                self.curr_stone_type, self.stones_to_remove = self.stones_to_remove, self.curr_stone_type
                self.turn = "white" if self.turn == "black" else "black"
            num_turns -= 1
        if num_turns > 0:
            raise ValueError("Invalid value for num_turns")


    def check_for_self_capture(self, pos):
        stone_group = self.get_stone_group(pos, self.curr_stone_type)
        for stone in stone_group:
            if self.has_liberties(stone):
                return
        self.set_position(pos, reset=True)
        raise ValueError("Self-capturing (suicide) is illegal")


    def move(self, *positions):
        for pos in positions:
            self.set_position(pos)
            enemy_neighbors = self.get_neighbors(pos, self.stones_to_remove)
            if enemy_neighbors:
                self.remove_stones(*enemy_neighbors)
            # use this to stop suicide
            self.check_for_self_capture(pos)
            self.pass_turn()



    def get_position(self, pos):
        row, col = self.get_coordinates(pos)
        return self.board[row][col]


    def check_for_illegal_ko(self):
        # impossible to have illegal ko before 5th move
        if len(self.game_states) > 4 and self.board == self.game_states[-3]:
            # if the turn was passed, it is not illegal KO, so check that last step != current step
            if self.board != self.game_states[-2]:
                self.rollback(1, illegal_ko=True)
                raise ValueError("Illegal KO move")


    def pass_turn(self):
        # append a copy of the board
        self.game_states.append([row[:] for row in self.board])
        self.check_for_illegal_ko()
        if self.turn == "black":
            self.turn = "white"
            self.stones_to_remove = self.black_piece
            self.curr_stone_type = self.white_piece
        elif self.turn == "white":
            self.turn = "black"
            self.stones_to_remove = self.white_piece
            self.curr_stone_type = self.black_piece
        else:
            raise ValueError("Value of turn should not be modified outside of this method")


    def print_board(self):
        height = self.size["height"]
        offset = "  "
        print(offset, end="")
        for i in range(self.size["width"]+1):
            # go boards skip the letter "I"
            if i == 8:
                continue
            print(" {}".format(chr(ord('A')+i)),end="")
        print("")
        for row in self.board:
            print("{}".format(height), end="")
            height -= 1
            if height < 9:
                print(" ", end='')
            for cell in row:
                print(" {}".format(cell), end="")
            print("")


    def reset(self):
        self.turn = "black"
        self.stones_to_remove = self.white_piece
        self.curr_stone_type = self.black_piece
        self.board = [["." for i in range(self.size["width"])] for j in range(self.size["height"])]
        self.game_states = [[row[:] for row in self.board]]
        self.handicap_stones_set = False


    def handicap_stones(self, num):
        if self.size["width"] != self.size["height"] or (self.size["height"] != 9 and self.size["height"] != 13 and self.size["height"] != 19):
            raise ValueError("Can't use handicap stones on non-square board")
        if num < 1:
            raise ValueError("Must specify a positive integer number of handicap stones")
        if self.size["width"] == 9 and num > 5:
            raise ValueError("Must specify a positive integer no greater than 5 for 9x9 board")
        if self.size["width"] == 13 and num > 9:
            raise ValueError("Must specify a positive integer no greater than 9 for 13x13 board")
        if self.size["width"] == 19 and num > 9:
            raise ValueError("Must specify a positive integer no greater than 9 for 19x19 board")
        if len(self.game_states) > 1:
            raise ValueError("Can't place handicap stones after game starts")
        if self.handicap_stones_set:
            raise ValueError("Can't place handicap stones more than once")

        self.hc_9x9 = {1:(2,6), 2:(6,2), 3:(6,6), 4:(2,2), 5:(4,4)}
        self.hc_13x13 = {1:(3,9), 2:(9,3), 3:(9,9), 4:(3,3), 5:(6,6), 6:(6,3), 7:(6,9), 8:(3,6), 9:(9,6)}
        self.hc_19x19 = {1:(3,15), 2:(15,3), 3:(15,15), 4:(3,3), 5:(9,9), 6:(9,3), 7:(9,15), 8:(3,9), 9:(15,9)}

        if self.size["width"] == 9:
            while num > 0:
                row, col = self.hc_9x9[num]
                self.board[row][col] = self.black_piece
                num -= 1
        elif self.size["width"] == 13:
            while num > 0:
                row, col = self.hc_13x13[num]
                self.board[row][col] = self.black_piece
                num -= 1
        elif self.size["width"] == 19:
            while num > 0:
                row, col = self.hc_19x19[num]
                self.board[row][col] = self.black_piece
                num -= 1

        self.handicap_stones_set = True
