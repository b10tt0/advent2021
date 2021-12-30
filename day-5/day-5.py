import re

data = open('input.txt', 'r', encoding='utf-8').read()
just_data = [int(i) for i in re.split(',|->| |\n', data) if i != '']
graph = [['.']*(max(just_data)+1) for i in range(max(just_data)+1)]
plus_5 = [['.']*(max(just_data)+1) for i in range(max(just_data)+1)]

print(just_data)

def print_graph():
    count = 0
    for line in graph:
        for index in line:
            count += 1
            print(index, end='')
        print('')

def get_coord(coord):
    return graph[coord[0]][coord[1]]

def add_to_plus_5(x, y):
    if graph[x][y] >= 2 and plus_5[x][y] == '.':
        plus_5[x][y] = 'X'

def count_plus_5(): 
    count = 0
    for x in plus_5:
        for i in x:
            if i == 'X':
                count += 1
    return count

def add_to_graph(s, e):
    diff = (e[0]-s[0], e[1]-s[1]) # assume a change
    print(diff)
    x_inc=y_inc=0
    if e[0] > s[0]: # if x increases
        x_inc = 1
    if e[0] < s[0]: # if x decreases
        x_inc = -1
    if e[0] == s[0]: # if x stays the same
        x_inc = 0

    if e[1] > s[1]:
        y_inc = 1
    if e[1] < s[1]:
        y_inc = -1
    if e[1] == s[1]:
        y_inc = 0
   
    r = max((abs(diff[0]), abs(diff[1]))) # range
    x, y = s[0], s[1]
    for i in range(r+1):
        if graph[y][x] == '.':
            graph[y][x] = 1
        else:
            graph[y][x] += 1
            add_to_plus_5(y, x)
        x += x_inc
        y += y_inc


i = 0
while i < len(just_data):
    s, e = (just_data[i],just_data[i+1]), (just_data[i+2],just_data[i+3])
    print(str(s) + '->' + str(e))
    add_to_graph(s, e)
    i+=4

print_graph()
print(count_plus_5())
