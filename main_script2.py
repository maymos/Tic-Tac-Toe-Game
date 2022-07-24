from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

from display_board import display_board
from clear_output import clear_output1
from player_input import player_input
from place_marker import place_marker
from win_check import win_check
from choose_first import choose_first
from space_check import space_check
from full_board_check import full_board_check
from player_choice import player_choice
from replay import replay




print('WELCOME TO TIC TAC TOE GAME!')

que = input('START TIC-TAC-TOE GAME? "Y" OR "N": ').upper()
while que=='Y':
    
    # SET GAME UP HERE
    clear_output1()
    test_board2 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player_1,player_2 = choose_first()
    game_on=True
    while game_on:
        
        
        pos_list = {0,1,2,3,4,5,6,7,8,9}
        pos_taken = {0}
        
        #PLAYER 1 PLAYING 
        if player_1==1:
            mark = player_input('Player 1')
            
            p1 = f'\nPLAYER 1: Your marker is=  "{mark[0]}"'
            p2 = f'PLAYER 2: Your marker is=  "{mark[1]}"\n'
            @interact(PLAYER_1 = p1, PLAYER_2 = p2)
            def display(PLAYER_1,PLAYER_2):
                return ''
            
            k = 1
            while full_board_check(test_board2)==False and k==1:
                
                #PLAYER 1 PAYING
                playr_repl=False
                while playr_repl==False:
                    print(f"Player_1: Choose a position to place Marker {mark[0]}")
                    
                    positn = player_choice(test_board2)
                    
                    #CHECK WHETHER THE POSITION CHOSEN IS FREE
                    if space_check(test_board2, positn)==True:
                        
                        pos_taken.add(positn)
                        place_marker(test_board2, mark[0], positn)
                        display_board(test_board2)
                        
                        #CHECK FOR WINNER
                        if win_check(test_board2, mark[0])=='win':
                            #print("PLAYER 1 WINS")
                            
                            p1 = "     CONGRATULATIONS!     "
                            p2 = "PLAYER 1 IS THE WINNER "
                            @interact(PLAYER_1 = p1, PLAYER_2 = p2)
                            def display(PLAYER_1,PLAYER_2):
                                return ''
                            
                            k=0
                            game_on=False
                            break
                            
                        #IF THE BOARD IS FULL AND NO WINNER; GAME TIE
                        elif full_board_check(test_board2)==True:
                            
                            p1 = "       *** DRAW GAME ***       "
                            p2 = '     THE GAME IS A TIE     '                         
                            @interact(PLAYER_1 = p1, PLAYER_2 = p2)
                            def display(PLAYER_1,PLAYER_2):
                                return ''
                            
                            game_on=False
                            break
                        else:
                            pass
                        playr_repl=True
                        break
                        
                    #IF POSITION HAS BEEN OCCUPIED, ASK TO CHOOSE ANOTHER POSITION
                    else:
                        pos_rem = pos_list-pos_taken
                        print(f'Position Taken, Choose another Position between {pos_rem}')
                        continue
                    
                #PLAYER 2 PAYING 
                while playr_repl:
                    if full_board_check(test_board2)==True and k==1:
                        game_on=False
                        break
                    print(f"Player_2: Choose a position to place Marker {mark[1]}")
                    positn = player_choice(test_board2)
                    
                    #CHECK WHETHER THE POSITION CHOSEN IS FREE
                    if space_check(test_board2, positn)==True:
                        
                        pos_taken.add(positn)
                        place_marker(test_board2, mark[1], positn)
                        display_board(test_board2)
                        
                        #CHECK FOR WINNER
                        if win_check(test_board2, mark[1])=='win':
                            #print("PLAYER 2 WINS")
                            
                            p1 = "     CONGRATULATIONS!     "
                            p2 = "PLAYER 2 IS THE WINNER "
                            @interact(PLAYER_1 = p1, PLAYER_2 = p2)
                            def display(PLAYER_1,PLAYER_2):
                                return ''
                            
                            k=0
                            game_on=False
                            break
                            
                        #IF THE BOARD IS FULL AND NO WINNER; GAME TIE
                        elif full_board_check(test_board2)==True:
                            p1 = "       *** DRAW GAME ***       "
                            p2 = '     THE GAME IS A TIE     '                         
                            @interact(PLAYER_1 = p1, PLAYER_2 = p2)
                            def display(PLAYER_1,PLAYER_2):
                                return ''
                            game_on=False
                            break
                        else:
                            pass
                        playr_repl=True
                        break
                        
                    #IF POSITION HAS BEEN OCCUPIED, ASK TO CHOOSE ANOTHER POSITION
                    else:
                        pos_rem = pos_list-pos_taken
                        print(f'Position Taken, Choose another Position between {pos_rem}')
                        continue
                        
        #IF PLAYER 2 IS PLAYING FIRST, ITERATION STARTS FROM HERE
        else:
            j=1
            print('\nPLAYER_2==1\n')
                    
            mark = player_input('Player 2')
            
            p1 = f'\nPLAYER 1: Your marker is=  "{mark[1]}"'
            p2 = f'PLAYER 2: Your marker is=  "{mark[0]}"\n'
            @interact(PLAYER_1 = p1, PLAYER_2 = p2)
            def display(PLAYER_1,PLAYER_2):
                return ''
            
            #print(f'Player 2: Your marker is {mark[0]}')
            while full_board_check(test_board2)==False and j==1:                         
                    
                #PLAYER 1 PAYING
                playr_repl=False
                while playr_repl==False:
                        
                    print(f"Player_2: Choose a position to place Marker {mark[0]}")
                    positn = player_choice(test_board2)
                    
                    #CHECK WHETHER THE POSITION CHOSEN IS FREE
                    if space_check(test_board2, positn)==True: 
                        
                        pos_taken.add(positn)
                        place_marker(test_board2, mark[0], positn)
                        display_board(test_board2)
                        
                        #CHECK FOR WINNER
                        if win_check(test_board2, mark[0])=='win':
                            #print("PLAYER 2 WINS")
                            
                            p1 = "     CONGRATULATIONS!     "
                            p2 = "PLAYER 2 IS THE WINNER "
                            @interact(PLAYER_1 = p1, PLAYER_2 = p2)
                            def display(PLAYER_1,PLAYER_2):
                                return ''
                            
                            j=0
                            game_on=False
                            break
                            
                        #IF THE BOARD IS FULL AND NO WINNER; GAME TIE
                        elif full_board_check(test_board2)==True:
                            p1 = "       *** DRAW GAME ***       "
                            p2 = '     THE GAME IS A TIE     '                         
                            @interact(PLAYER_1 = p1, PLAYER_2 = p2)
                            def display(PLAYER_1,PLAYER_2):
                                return ''
                            game_on=False
                            break
                            
                        else:
                            pass
                        playr_repl=True
                        break
                    
                    #IF POSITION HAS BEEN OCCUPIED, ASK TO CHOOSE ANOTHER POSITION
                    else:
                        pos_rem = pos_list-pos_taken
                        print(f'Position Taken, Choose another Position between {pos_rem}')
                        continue

                #PLAYER 2 PAYING 
                while playr_repl:
                    if full_board_check(test_board2)==True and j==1:
                        game_on=False
                        break
                    print(f"Player_1: Choose a position to place Marker {mark[1]}")
                    positn = player_choice(test_board2)
                    
                    #CHECK WHETHER THE POSITION CHOSEN IS FREE
                    if space_check(test_board2, positn)==True:
                        pos_taken.add(positn)
                        place_marker(test_board2, mark[1], positn)
                        display_board(test_board2)
                        
                        #CHECK FOR WINNER
                        if win_check(test_board2, mark[1])=='win':
                            #print("PLAYER 1 WINS")
                            
                            p1 = "     CONGRATULATIONS!     "
                            p2 = "PLAYER 1 IS THE WINNER "
                            @interact(PLAYER_1 = p1, PLAYER_2 = p2)
                            def display(PLAYER_1,PLAYER_2):
                                return ''
                            
                            j=0
                            game_on=False
                            break
                        
                        #IF THE BOARD IS FULL AND NO WINNER; GAME TIE
                        elif full_board_check(test_board2)==True:
                            p1 = "       *** DRAW GAME ***       "
                            p2 = '     THE GAME IS A TIE     '                      
                            @interact(PLAYER_1 = p1, PLAYER_2 = p2)
                            def display(PLAYER_1,PLAYER_2):
                                return ''
                            game_on=False
                            break
                        
                        else:
                            pass
                        playr_repl=True
                        break
                        
                    #IF POSITION HAS BEEN OCCUPIED, ASK TO CHOOSE ANOTHER POSITION
                    else:
                        pos_rem = pos_list-pos_taken
                        print(f'Position Taken, Choose another Position between {pos_rem}')
                        continue
                        
                if full_board_check(test_board2)==True:
                    break
        
#ASK WHETHER TO REPLAY GAME AGAIN
    if not replay():
        print('\n******************************************************')
        print('||    THANK YOU FOR PLAYING TIC-TAC-TOE GAME!!!     ||')
        print('******************************************************')
        break