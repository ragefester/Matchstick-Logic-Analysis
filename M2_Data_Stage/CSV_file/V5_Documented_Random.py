# This is the user friendly code

# V5
# 2 computer players iterative
# Focus is to gather useful data and graph it
# Most code copied from V4
# Streamlined to be computer friendly

import random

'''Make move'''
# Determines who's turn it is
def ask_input(pl1):
    if pl1:
        print("CPU1's turn")
    else:
        print("CPU2's turn")
    return CPU_move()      

#CPU move taken from V2
def CPU_move():
    Cpu_response = random.randint(1,3)
    return Cpu_response

#Processing the value picked by the human and returning what numbers remain
def player_move(game_lst, move_chosen):
    print(f'Number Picked: {move_chosen}')
    del game_lst[:move_chosen]
    print("Numbers remaining: ", game_lst)
    return game_lst

'''Check if game ended'''
# Check to see who was won the game
def check_win(lst):
    # Working with bools, len(lst) should be 0 if game is finished, therefore not 0 will be 1.
    if not len(lst):
        print('Game Over')
    # Only returns True if list is empty
    return len(lst) == 0

# Checks to see who has won
def check_player_winner(pl1):
    if not pl1:
        winner = '1'
    else:
        winner = '2'
    print(f"Player {winner} has won the game.")

'''Records moves in game and displays'''
# This adds chunks of the original list to another list in sections
def add_to_list(lst_allmoves, lst_availablemoves, val):
    lst_allmoves.append(lst_availablemoves[:val])
    return lst_allmoves

# Extracts player's moves
def pl1_history(lst, pl1_lst):
    for i in range(len(lst)):
        if i % 2 == 0:
            pl1_lst.append(lst[i])
    return pl1_lst

def pl2_history(lst, pl2_lst):
    for i in range(len(lst)):
        if i % 2 == 1:
            pl2_lst.append(lst[i])
    return pl2_lst

'''Counts wins and logs values picked'''
# Logs number picked by both players in a game
def all_pl_values(n, lst_of_values):
    lst_of_values.append(n)

#Counts how many wins player 1 has
def count_pl1_wins(win):
    win.append('p1')

#Counts how many wins player 2 has
def count_pl2_wins(win):
    win.append('p2')
''''''
# Driver code
def main():
    #We first set the limit of the game
    win_condition = 15

    # Choosing how many iterations we want
    iterations = 10#int(input('How many iterations? '))

    #Tidying things up a bit, keep track of who won
    all_values_picked, winner_list = [], []
    
    #Iterates until game is over
    for i in range(iterations):
        # ALL OF THESE VARIABLES NEED TO BE RE-INITIALISED EACH ITERATION
        # Putting this inside the loop this time because I want to gather data on 1 player always going first
        player1 = True

        #Setting the list of numbers
        available_moves = [i for i in range(win_condition+1)]
        available_moves.remove(0)

        # Log each player's individual value per move
        pl1_values, pl2_values = [], []

        #Log of each player's moves per game
        pl1_moves, pl2_moves, = [], []

        # All moves IN ONE GAME
        all_moves = []

        # Provides clarity when reading console
        print()
        print(f'This is iteration number {i+1}.')

        while True:

            #Prompts user for how many moves
            num_moves = ask_input(player1)

            # Logs what value CPU picked
            if not player1:
                all_pl_values(num_moves, pl1_values)
            else:
                all_pl_values(num_moves, pl2_values)

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
                player1_moves = pl1_history(every_move, pl1_moves)

                #Find which moves are pl2
                player2_moves = pl2_history(every_move, pl2_moves)

                # Same as above, looking for who doesn't pick the last number
                if not player1: 
                    count_pl1_wins(winner_list)
                else:
                    count_pl2_wins(winner_list)
                break

            else:
                #Change player
                player1 = not player1
        all_pl_values(pl1_values, all_values_picked)
        all_pl_values(pl2_values, all_values_picked)

    # Logs all moves per player over all games
    count = 0
    all_player1_moves, all_player2_moves = [], []
    while count < len(all_values_picked):
        if count % 2 == 0:
            all_player1_moves.append(all_values_picked[count])
        else:
            all_player2_moves.append(all_values_picked[count])
        count += 1

    # Display every set of games and moves played by each player
    print()
    print(all_player1_moves)
    print(all_player2_moves)
    # Display who won each game
    print(winner_list)

    '''Storing the data'''
    lines = winner_list
    with open('M2_Data_Stage/CSV_file/V5_wins.csv', 'w') as file:
        for i in lines:
            file.write(i)
            file.write(',')

    lines1 = all_player1_moves
    lines2 = all_player2_moves
    with open('M2_Data_Stage/CSV_file/V5_moves.csv', 'w') as file:
        for i in lines1:
            for j in i:
                file.write(str(j))
                file.write(',')
            file.write(' ,')
        file.write('\n')
        for i in lines2:
            for j in i:
                file.write(str(j))
                file.write(',')
            file.write(' ,')
        
#Call game
main()