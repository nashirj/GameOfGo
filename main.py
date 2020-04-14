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




test_illegal_ko()
