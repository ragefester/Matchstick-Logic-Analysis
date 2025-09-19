# Only works in a 3 value game

import csv
import plotly.graph_objs as go
import plotly.io as pio

# This code results in 2 single lists with games separated 
total_list = []
with open('M2_Data_Stage/CSV_file/V5_moves.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row != []:
            total_list.append(row)
nums_list1 = total_list[0] 
nums_list2 = total_list[1]

# Counts moves by a.Random and b.Optimised
# Works when 3 values available per move
a1,a2,a3,b1,b2,b3 = 0,0,0,0,0,0
for i in nums_list1:
    a1 += i.count('1')
    a2 += i.count('2')
    a3 += i.count('3')
for i in nums_list2:
    b1 += i.count('1')
    b2 += i.count('2')
    b3 += i.count('3')

# Plots the data on a bar chart
values = [a1,a2,a3,b1,b2,b3]
fig = go.Figure()
fig.add_trace(go.Bar(x=['CPU1:1','CPU1:2','CPU1:3','CPU2:1','CPU2:2','CPU2:3'], y=values))
fig.update_layout(
    title='Moves per player',
    xaxis_title='Number 1,2,3',
    yaxis_title='Frequency'
)
pio.show(fig)