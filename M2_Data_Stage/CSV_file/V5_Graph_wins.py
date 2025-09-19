'''
# if wins is in 999,1000 form
values = []
temp = ''
with open('V5_wins.csv', 'r') as file:
    content = file.read()
    print(content)
    for i in content:
        if i == ',':
            values.append(int(temp))
            temp = ''
        else:
            temp += i
    values.append(int(temp))
'''
#if wins is in '1', '2' form
import plotly.io as pio

pl1_wins = 0
pl2_wins = 0
with open('M2_Data_Stage/CSV_file/V5_wins.csv', 'r') as file:
    content = file.read()
    for i in content:
        if i == '1':
            pl1_wins += 1
        elif i == '2':
            pl2_wins += 1
            
values = [pl1_wins, pl2_wins]
colours = ['#FF0000', '#0000FF']

trace1 = {'values': values,
'marker': {'colors': colours},
'labels': ['Player1', 'Player2'],
'type': 'pie',
'hole': .7,
'showlegend': True}
pio.show({'data': [trace1]})
