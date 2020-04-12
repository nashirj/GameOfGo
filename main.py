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




game = Go(9)
moves = ["4H","8A","8B"]
# i = 1
# for move in moves:
#     print("move {}\n".format(i))
#     # try:
#     game.move(move)
#     # except:
#     #     print("raised self capture error")
#     game.print_board()
#     print("")
#     i += 1

# game.pass_turn()
# game.pass_turn()

game.move(*["8F","5G","1A"])

# assert game.get_position("9A") == "."
# game.move("3B")
# assert game.get_position("3B") == "x"
# # test.assert_equals(game.get_position("9A"), ".", "Illegal stone should be removed")
# # game.move("3B")
# # test.assert_equals(game.get_position("3B"), "x", "Black should have another try")


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


# game = Go(5)
# moves = ["5C","5B","4D","4A","3C","3B",
#          "2D","2C","4B","4C","4B"]
# # test.expect_error("Illegal KO move. Should throw an error.", lambda: game.move(*moves))
# i = 1
# for move in moves:
#     print("move {}\n".format(i))
#     try:
#         game.move(move)
#     except:
#         print("raised ko error")
#     game.print_board()
#     print("")
#     print("turn: " + game.turn)
#     i += 1

# game.move("2B")
# game.print_board()


# print("Testing handicap")

# for i in range(1,6):
#     game = Go(9)
#     game.handicap_stones(i)
#     game.print_board()

# for i in range(1,10):
#     game = Go(13)
#     game.handicap_stones(i)
#     game.print_board()

# for i in range(1,10):
#     game = Go(19)
#     game.handicap_stones(i)
#     game.print_board()


# game = Go(19)
# game.move("16E")
# game.print_board()

# game = Go(9)
# captured = ["6D", "6E", "4D", "5D", "5C", "4E", "3E","3F","2F","2G","1G","4C"]
# game.move(*moves)