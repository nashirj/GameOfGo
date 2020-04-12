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



# game = Go(9)
# moves = ["5D","5E","4E","6E","7D","4F","7E","3E","5F","4D",
#          "6F","6D","6C","7F","4E","5E"]

# i = 1
# for move in moves:
#     print("move {}\n".format(i))
#     game.move(move)
#     game.print_board()
#     print("")
#     i += 1

# game.rollback(3)


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
    i += 1

game.move("2B")
game.print_board()
# test.assert_equals(game.get_position("2B"), "x", "Black should be given another try to place their stone.")
# test.assert_equals(game.get_position("4B"), ".", "Should rollback game before illegal move was made.")
# close_it()






# game = Go(9)
# captured = ["6D", "6E", "4D", "5D", "5C", "4E", "3E","3F","2F","2G","1G","4C"]
# game.move(*moves)