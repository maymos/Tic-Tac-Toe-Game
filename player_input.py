def player_input(playr):
    h = True
    while h:
        marker = input(f'{playr} Choose a Marker "X" or "O": ').upper()
        if marker=='X':
            return ('X','O')
            h=False
            break
        elif marker=='O':
            return ('O','X')
            h=False
            break
        else:
            print('Enter Correct Letter: "X" or "O"')
            continue

#print(player_input('Mayowa'))