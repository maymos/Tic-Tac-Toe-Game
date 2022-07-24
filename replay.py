def replay():
    my_replay = True
    while my_replay:
        repl = input('Play Again "Y" or "N": ').upper()
        if repl=="Y":
            return True
        elif repl=='N':
            return False
        else:
            print('Choose Yes = "Y" or No = "N" to Replay or Quit')
            continue