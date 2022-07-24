def space_check(board, position):
    try:
        if board[position]==' ':
            return True
    except TypeError:
        print('All Position Occupied')
    else:
        return False