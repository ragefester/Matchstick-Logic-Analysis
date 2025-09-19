import random
import plotly.io as pio 

def Random_CPU_move():
    return random.randint(1,3)

def Optimised_CPU_move(number):
    # List of losing numbers for this game
    losing_list = [1, 5, 9, 13]
    n = 0
    # Find the losing number below the number the game is on
    for i in losing_list:
        if number > i:
            n += 1
    if number in losing_list:
        return random.randint(1,3)
    elif number > 5:
        losing_number_below = 4*n - 3
        move = number - losing_number_below
        return move
    else:
        # Won't return 0 as 1 is in losing list
        move = number - 1
        return move

def check_win(condition):
    return condition < 1
# Count wins
def count_wins(turn, pl1_count):
    # If you end the game, you lose
    if not turn:
        pl1_count += 1
    return pl1_count

def main():
    pl1_wins = 0
    ###############
    iterations = 10000
    ################
    for i in range(iterations):
        win_condition = 15
        # Player 1 starts every game
        player1 = True
        while True:
            #Make move
            if player1:
                move = Random_CPU_move()
            else:
                move = Optimised_CPU_move(win_condition)
            #Executes move
            win_condition -= abs(move)
            #Check if game is won
            if check_win(win_condition):
                pl1_wins = count_wins(player1, pl1_wins)
                break
            else:
                # Change player
                player1 = not player1

    # Set up the plot
    colours = ['#FF0000', '#0000FF']
    trace = {'values': [pl1_wins, iterations-pl1_wins],
    'marker': {'colors': colours},
    'labels': ['Random', 'Optimal'],
    'type': 'pie',
    'hole': .7,
    'showlegend': True}
    pio.show({'data': [trace]})


if __name__ == "__main__":
    main()