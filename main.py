from Go import Go

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
    if i == 8:
        stone_group = game.get_stone_group("6E", 'o')
        print(stone_group)
        exit()



# game = Go(9)
# captured = ["6D", "6E", "4D", "5D", "5C", "4E", "3E","3F","2F","2G","1G","4C"]
# game.move(*moves)