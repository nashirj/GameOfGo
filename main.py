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
moves = ["5D","5E","4E","6E","7D","4F","7E","3E","5F","4D",
         "6F","6D","6C","7F","4E","5E"]

i = 1         
for move in moves:
    # print("move {}\n".format(i))
    game.move(move)
    # game.print_board()
    # print("")
    i += 1

game.rollback(3)






# game = Go(9)
# captured = ["6D", "6E", "4D", "5D", "5C", "4E", "3E","3F","2F","2G","1G","4C"]
# game.move(*moves)