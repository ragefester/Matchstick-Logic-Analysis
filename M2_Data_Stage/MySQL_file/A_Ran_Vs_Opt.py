# this is modified code from V7 that outlines how we want our AI to play
# this is a random v opt, random goes first
import random
import pandas as pd
# Optimised Formula
def Optimised_CPU_move(number):
    length = number // 4
    losing_list = [1, 5, 9, 13]
    if number in losing_list:
        return random.randint(1,3)
    elif number > 5:
        losing_number_below = 5 + (length-1)*4
        move = number - losing_number_below
        return abs(move)
    else:
        move = number - 1
        return abs(move)

def Random_CPU_move():
    return random.randint(1,3)

def player_move(game_number, move_chosen):
    game_number -= move_chosen
    return game_number

def check_win(game_number):
    return game_number < 1

def main():
    iterations = 10000 #int(input('How many iterations? '))
    winner_list = []
    #Technically the game can only go to 15 move with two random
    move1, move2, move3, move4, move5, move6, move7, move8, move9, move10, move11, move12, move13, move14, move15 = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    for i in range(iterations):
        count = 0
        win_condition = 15
        player1 = True
        # Iterates over until game is finished
        while True:
            count+= 1
            # Player 2 is optimised
            if player1: 
                num_chosen = Random_CPU_move()
                #print(f'Random move: {num_chosen}')
            else: 
                num_chosen = Optimised_CPU_move(win_condition)
                #print(f'Optimised move: {num_chosen}')
            # Messy but works
            if count == 1: move1.append(float(num_chosen))
            elif count == 2: move2.append(float(num_chosen))
            elif count == 3: move3.append(float(num_chosen))
            elif count == 4: move4.append(float(num_chosen))
            elif count == 5: move5.append(float(num_chosen))
            elif count == 6: move6.append(float(num_chosen))
            elif count == 7: move7.append(float(num_chosen))
            elif count == 8: move8.append(float(num_chosen))
            elif count == 9: move9.append(float(num_chosen))
            elif count == 10: move10.append(float(num_chosen))
            elif count == 11: move11.append(float(num_chosen))
            elif count == 12: move12.append(float(num_chosen))
            elif count == 13: move13.append(float(num_chosen))
            elif count == 14: move14.append(float(num_chosen))
            elif count == 15: move15.append(float(num_chosen))
            # Execute move
            win_condition = player_move(win_condition, num_chosen)
            #print(f'Game: {win_condition}')
            #Check if game is won
            if check_win(win_condition):
                # Counts win for opt player
                if player1: 
                    winner_list.append(1)
                else:
                    winner_list.append(0)
                break
            # Change player
            else:
                player1 = not player1
        #Again, Definitely not optimal but it works
        while len(move8) < len(move1):
            move8.append(0.0)
        while len(move9) < len(move1):
            move9.append(0.0)
        while len(move10) < len(move1):
            move10.append(0.0)
        while len(move11) < len(move1):
            move11.append(0.0)
        while len(move12) < len(move1):
            move12.append(0.0)
        while len(move13) < len(move1):
            move13.append(0.0)
        while len(move14) < len(move1):
            move14.append(0.0)
        while len(move15) < len(move1):
            move15.append(0.0)

    df = pd.DataFrame({
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
    'move10': move10,
    'move11': move11,
    'move12': move12,
    'move13': move13,
    'move14': move14,
    'move15': move15,
    })

#sql2 = "INSERT INTO compile (wins, move1, move2, move3, move4, move5, move6, move7, move8, move9, move10, move11, move12, move13, move14, move15) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)"
#wins, move1, move2, move3, move4, move5, move6, move7, move8, move9, move10, move11, move12, move13, move14, move15
    

    import mysql.connector
    # Credentials, an use list as well
    config = {
        "host":r"localhost",
        "user":r"sample_user",
        "password":r"sample_password",
        "database":r"data_holder"
    }
    # Connect to database, ** as we are connection with a dictionary
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    # Prepare data in pandas dataframe to be inserted into database
    sql_data = [tuple(row) for row in df.values]
    # Clear the database (compile) of any existing  data
    sql1 = "TRUNCATE TABLE data_holder.compile"
    # As there are 16 columns, it is cleaner to use join method
    sql2 = f"INSERT INTO compile ({', '.join(df.columns)}) VALUES ({', '.join(['%s'] * len(df.columns))})"
    cursor.execute(sql1)
    cursor.executemany(sql2, sql_data)
    connection.commit()
    # Close connection
    cursor.close()
    connection.close()

main()