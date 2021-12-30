import re

data = open('input.txt', 'r', encoding='utf-8').read()
just_data = [int(i) for i in re.split(',|->| |\n', data) if i != '']
graph = [['.']*(max(just_data)+1) for i in range(max(just_data)+1)]

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

def add_to_graph(s, e):
    diff = (e[0]-s[0], e[1]-s[1])
    if diff[0] == 0: # if y changes
        if diff[1] > 0:
            r = (s[1], e[1]+1)
        else:
            r = (e[1], s[1]+1)
        for y in range(r[0], r[1]):
            if graph[y][s[0]] == '.':
                graph[y][s[0]] = 1
            else:
                graph[y][s[0]] += 1
            
    else: # if x change
        if diff[0] > 0:
            r = (s[0], e[0]+1)
        else:
            r = (e[0], s[0]+1)
        for x in range(r[0], r[1]):
            if graph[s[1]][x] == '.':
                graph[s[1]][x] = 1
            else:
                graph[s[1]][x] += 1

i = 0
while i < len(just_data):
    s, e = (just_data[i],just_data[i+1]), (just_data[i+2],just_data[i+3])
    if s[0] == e[0] or s[1] == e[1]: 
        print(str(s) + '->' + str(e))
        add_to_graph(s, e)
    i+=4

print_graph() 
