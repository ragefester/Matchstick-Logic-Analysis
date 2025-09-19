#V2
#Two computers pick random values
#Once through

import random

def display_player(pl1):
    if pl1:
        print("Computer 1's turn")
    else:
        print("Computer 2's turn")

def ask_input(pl1):
    if pl1:
        return CP1_move()
    else:
        return CP2_move()        

#CP1 and CP2 decisions will be the same code for this Version 
def CP1_move():
    Cpu1 = random.randint(1,3)
    return Cpu1

def CP2_move():
    Cpu2 = random.randint(1,3)
    return Cpu2

def player_move(lst, n_moves):
    print(f'Number Picked: {n_moves}')
    print("Numbers picked: ", lst[:n_moves])
    del lst[:n_moves]
    print("Numbers remaining: ", lst)
    return lst

def check_win(lst):
    if not len(lst):
        print('Game Over')
    return len(lst) == 0

def check_player_winner(pl1):
    if not pl1:
        winner = '1'
    else:
        winner = '2'
    print(f"Player {winner} has won the game.")

def add_to_list(every, lst, num_moves):
    every.append(lst[:num_moves])
    return every

def pl1_history(lst, pl1_lst):
    for i in range(len(lst)):
        if i % 2 == 0 or i == 0:
            pl1_lst.append(lst[i])
    return pl1_lst

def pl2_history(lst, pl2_lst):
    for i in range(len(lst)):
        if i % 2 == 1:
            pl2_lst.append(lst[i])
    return pl2_lst

def main():
    win_condition = 15
    player1 = True
    all_moves = []
    pl1_moves = []
    pl2_moves = []
    available_moves = [i for i in range(win_condition+1)]
    available_moves.remove(0)
    
    while True:
        #Shows who's turn it is
        display_player(player1)
        #Prompts user for how many moves
        num_moves = ask_input(player1)
        # Adds move to list
        every_move = add_to_list(all_moves, available_moves, num_moves)
        #Executes move
        player_move(available_moves, num_moves)

        #Check if game is won
        if check_win(available_moves):
            print()
            #Check who has won
            check_player_winner(player1)
            #Find which moves are pl1
            pl1_moves = pl1_history(every_move, pl1_moves)
            #Find which moves are pl2
            pl2_moves = pl2_history(every_move, pl2_moves)
            print('Moves by Player 1: ', pl1_moves)
            print('Moves by Player 2: ',pl2_moves)
            break
        else:
            #Change player
            player1 = not player1
    

main()