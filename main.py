from Go import Go


def print_games(game):
    for board in game.game_states:
        print(" ", end="")
        for i in range(game.width):
            print(" {}".format(chr(ord('A')+i)),end="")
        print("")
        height = game.height
        for row in board:
            print("{}".format(height), end="")
            height -= 1
            for cell in row:
                print(" {}".format(cell), end="")
            print("")


def test_rollback():
    game = Go(9)
    moves = ["5D","5E","4E","6E","7D","4F","7E","3E","5F","4D",
             "6F","6D","6C","7F","4E","5E"]

    i = 1
    for move in moves:
        print("move {}\n".format(i))
        game.move(move)
        game.print_board()
        print("")
        i += 1

    # game.print_board()
    # print('\n')

    i = 3
    print("\n\nROLLING BACK {} turns\n\n".format(i))
    game.rollback(i)

    print('\n')

    game.move("4E")
    game.print_board()
    print("")


def test_illegal_ko():
    game = Go(5)
    moves = ["5C","5B","4D","4A","3C","3B",
             "2D","2C","4B","4C","4B"]
    # test.expect_error("Illegal KO move. Should throw an error.", lambda: game.move(*moves))
    i = 1
    for move in moves:
        print("move {}\n".format(i))
        try:
            game.move(move)
        except:
            print("raised ko error")
        game.print_board()
        print("")
        print("turn: " + game.turn)
        i += 1
    # game.move("2B")
    # game.print_board()


def test_correct_turn_after_multiple_rollbacks():
    game = Go(9)
    moves = ["5C","5G","4D"]
    i = 1
    for move in moves:
        print("move {}\n".format(i))
        # try:
        game.move(move)
        # except:
            # print("raised ko error")
        game.print_board()
        print("")
        print("turn: " + game.turn)
        i += 1

    game.rollback(2)
    i -= 2
    
    moves = ["8F","5G","1A"]
    # test.expect_error("Illegal KO move. Should throw an error.", lambda: game.move(*moves))
    for move in moves:
        print("move {}\n".format(i))
        try:
            game.move(move)
        except:
            print("raised ko error")
        game.print_board()
        print("")
        print("turn: " + game.turn)
        i += 1
    


def test_handicap():
    print("Testing handicap")
    for i in range(1,6):
        game = Go(9)
        game.handicap_stones(i)
        game.print_board()

    for i in range(1,10):
        game = Go(13)
        game.handicap_stones(i)
        game.print_board()

    for i in range(1,10):
        game = Go(19)
        game.handicap_stones(i)
        game.print_board()


def test_random():
    game = Go(20, 6)
    moves=["2A","1A","17D","9A","5E","11D","10B","2E","3E","6E","1D","15E","19A","17B","7A","14D","15D"]
    game.move(*moves)
    game.print_board()
    game.rollback(3)
    moves=["11B","17A","2B","1C","7C","7D","9B","6D","1B","18B","4A","19C","8D","9E","7E","16B","14C"]
    game.move(*moves)
    game.print_board()
    game.rollback(5)
    moves = ["15A","18E","4C","7B","9D","8B","15B","17E","14E","2D","5B","12C","13E","13D","3C","8E","9C","3B","16E","12D","2C","19E","10C","12E","12A","19B","3D","8C","19D","18A","13A","1E","4E","16D","18D","14B","5D","6B","13B","4B"]
    game.move(*moves)
    game.print_board()
    moves=["13C"]
    game.move(*moves)
    game.print_board()
    moves = ["4D"]
    game.move(*moves)
    game.rollback(7)
    moves = ["17C","11A","10E","5C","16C","11E","5A","6C"]
    game.move(*moves)


# test_illegal_ko()
# test_correct_turn_after_multiple_rollbacks()
test_random()
