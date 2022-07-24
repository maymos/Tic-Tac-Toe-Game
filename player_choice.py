def player_choice(board):
    m=True 
    while m:
        try:
            sel_pos = int(input(''))
            return sel_pos
        except ValueError:
            print('CHOOSE INTEGER BETWEEN (1-9)')
            continue