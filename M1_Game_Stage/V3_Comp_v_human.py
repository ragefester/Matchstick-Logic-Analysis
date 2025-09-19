#V3
#One computers pick random values, One human player
#Once through (no iteration)
#Most code copied from V2

import random #For computer
# Determines who's turn it is
def ask_input(pl1):
    if pl1:
        print("Player's turn")
        return Human_move()
    else:
        print("Computer's turn")
        return CPU_move()      
# Human move taken from V1
def Human_move():
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
#CPU move taken from V2
def CPU_move():
    Cpu_response = random.randint(1,3)
    return Cpu_response

#Processing the value picked by the human and returning what numbers remain
def player_move(lst, n_moves):
    print(f'Number Picked: {n_moves}')
    print("Numbers picked: ", lst[:n_moves])
    del lst[:n_moves]
    print("Numbers remaining: ", lst)
    return lst

# Check to see who was won the game
def check_win(lst):
    # Working with bools, len(lst) should be 0 if game is finished, therefore not 0 will be 1.
    if not len(lst):
        print('Game Over')
    # Only returns True is list is empty
    return len(lst) == 0

# Checks to see who has won
def check_player_winner(pl1):
    if not pl1:
        winner = 'Human'
    else:
        winner = 'Computer'
    print(f"The {winner} has won the game.")

# This adds chunks of the original list to another list in sections
def add_to_list(every, lst, num_moves):
    every.append(lst[:num_moves])
    return every

# Extracts Player's moves
def pl1_history(lst, pl1_lst):
    for i in range(len(lst)):
        if i % 2 == 0 or i == 0:
            pl1_lst.append(lst[i])
    return pl1_lst

# Extracts computer's moves
def pl2_history(lst, pl2_lst):
    for i in range(len(lst)):
        if i % 2 == 1:
            pl2_lst.append(lst[i])
    return pl2_lst

# Driver code
def main():
    #We first set the limit of the game
    win_condition = 15
    player1 = True
    #Tidying things up a bit
    all_moves, pl1_moves, pl2_moves = [], [], []
    #Setting the list of numbers
    available_moves = [i for i in range(win_condition+1)]
    available_moves.remove(0)
    
    #Iterates until game is over
    while True:
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
            print('Moves CPU: ',pl2_moves)
            break
        else:
            #Change player
            player1 = not player1
#Call game
main()