# V5, Streamlined code, Nicer code in v5 copy, Down from 200 lines to 75
import random    

def CPU_move():
    Cpu_response = random.randint(1,3)
    return Cpu_response

def player_move(game_lst, move_chosen):
    del game_lst[:move_chosen]
    return game_lst

def check_win(lst):
    return len(lst) == 0

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

def count_pl1_wins(win):
    win.append('1')
def count_pl2_wins(win):
    win.append('2')

def main():
    win_condition = 15
    iterations = 100#int(input('How many iterations? '))
    winner_list = []
    pl1_values, pl2_values = [], []
    for i in range(iterations):
        player1 = True
        available_moves = [i for i in range(win_condition+1)]
        available_moves.remove(0)

        while True:
            num_moves = CPU_move()
            player_move(available_moves, num_moves)
            if player1:
                pl1_values.append(str(num_moves))
            else:
                pl2_values.append(str(num_moves))
            #Check if game is won
            if check_win(available_moves):
                if not player1: 
                    count_pl1_wins(winner_list)
                else:
                    count_pl2_wins(winner_list)
                pl1_values.append(' ')
                pl2_values.append(' ')
                break
            else:
                player1 = not player1
    print(winner_list)
    lines = winner_list
    with open('M2_Data_Stage/CSV_file/V5_wins.csv', 'w') as file:
        for i in lines:
            file.write(i)
            file.write(',')

    lines1 = pl1_values
    lines2 = pl2_values
    with open('M2_Data_Stage/CSV_file/V5_moves.csv', 'w') as file:
        for i in lines1:
            file.write(str(i))
            file.write(',')
        file.write('\n')
        for i in lines2:
            file.write(str(i))
            file.write(',')
main()