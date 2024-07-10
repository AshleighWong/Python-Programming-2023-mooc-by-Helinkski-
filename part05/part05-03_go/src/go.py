# Write your solution here
def who_won(game_board:list):
    piece1 = 0
    piece2 = 0
    for row in game_board:
        for item in row:
            if item == 1:
                piece1+=1
            elif item == 2:
                piece2 +=1
    if piece1 > piece2:
        return 1
    elif piece2 > piece1:
        return 2
    else:
        return 0