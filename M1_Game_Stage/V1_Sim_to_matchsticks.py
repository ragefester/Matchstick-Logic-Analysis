#V1
'''
Overview to problem:

1. First player starts at 1
2. Player can choose 1,2 or 3 numbers 
(they must be consecutive)
3. Turn switches
4. Player who chooses 15 loses

Plan/Pseudocode:

1. Set up two players
2. Set parametres
3. Have different functions with specific tasks
4. Iterate over until win condition is met
5. Store and compile data
'''

#Takes no args
def ask_input(): 
    while True:
        n_moves = input("Please enter number of moves (1,2,3): ")
        try: 
            if int(n_moves) < 4 and int(n_moves) > 0:
                return int(n_moves)
                break
            else:
                print('Please enter a valid value. ')
        except ValueError:
            print('Please enter a valid value. ')

#Takes player1 as arg
def display_player(pl1):
    if pl1:
        print("Player 1's turn")
    else:
        print("Player 2's turn")

#Takes player as arg
def check_player_winner(pl1):
    if not pl1:
        winner = '1'
    else:
        winner = '2'
    print(f"Player {winner} has won the game.")

#Takes moves as arg
def check_win(lst):
    if not len(lst):
        print('Game Over')
    return len(lst) == 0

#Takes moves as arg
def player_move(lst, num_moves):
    print("Numbers picked: ", lst[:num_moves])
    del lst[:num_moves]
    print("Numbers remaining: ", lst)
    return lst

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
        num_moves = ask_input()
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