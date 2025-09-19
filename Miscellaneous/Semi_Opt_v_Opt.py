import random
import pandas as pd

'''These were changed for all the variants in the AI analysis'''

def Optimised_CPU_move(number):
    losing_list = [1, 5, 9, 13]
    n = 0
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

def Semi_Optimised_CPU_move(number):
    a = random.randint(1,2)
    if a == 1:
        losing_list = [1, 5, 9, 13]
        n = 0
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
    else:
        return random.randint(1,3)
    
def check_win(condition):
    return condition < 1
# Count wins
def count_wins(turn, pl1_count):
    if turn:
        pl1_count += 1
    return pl1_count

def main():
    pl1_wins = 0
    ####################
    iterations = 100
    ####################

    winner_list = []
    move1, move2, move3, move4, move5, move6, move7, move8, move9 = [],[],[],[],[],[],[],[],[]

    for i in range(iterations):
        win_condition = 15
        count = 1

        #player1 = True
        #'''
        b = random.randint(1,2)
        if b == 1:
            player1 = True
        else:
            player1 = False
        #'''
        while True:
            #Ran pl1, Opt pl2
            if player1:
                move = Semi_Optimised_CPU_move(win_condition)
            else:
                move = Optimised_CPU_move(win_condition)
            if count == 1: move1.append(float(move))
            elif count == 2: move2.append(float(move))
            elif count == 3: move3.append(float(move))
            elif count == 4: move4.append(float(move))
            elif count == 5: move5.append(float(move))
            elif count == 6: move6.append(float(move))
            elif count == 7: move7.append(float(move))
            elif count == 8: move8.append(float(move))
            elif count == 9: move9.append(float(move))

            #Executes move
            win_condition -= abs(move)
            #Check if game is won
            if check_win(win_condition):

                if player1: 
                    winner_list.append(1)
                if not player1:
                    winner_list.append(0)

                pl1_wins = count_wins(not player1, pl1_wins)

                if len(move7) != len(move1):
                    move7.append(0.0)
                if  len(move8) != len(move1):
                    move8.append(0.0)
                if  len(move9) != len(move1):
                    move9.append(0.0)
                break
            else:
                player1 = not player1
                count += 1

    print(iterations)
    print(iterations - pl1_wins)

    data = pd.DataFrame({
    'wins': winner_list,
    'move1': move1,
    'move2': move2,
    'move3': move3,
    'move4': move4,
    'move5': move5,
    'move6': move6,
    'move7': move7,
    'move8': move8,
    'move9': move9,
    })

    data.to_csv(r'Miscellaneous/df_game.csv', index=False)

if __name__ == "__main__":
    main()