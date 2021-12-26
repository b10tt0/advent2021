"""
- forward X increases the horizontal position by X units.
- down X increases the depth by X units.
- up X decreases the depth by X units.
"""

data = open('input.txt', 'r', encoding='utf-8').read().splitlines()
directions = [(i[:-1], int(i[-1])) for i in data]

horizontal = sum(i[1] for i in directions if i[0] == 'forward ')
up = sum(i[1] for i in directions if i[0] == 'up ')
down = sum(i[1] for i in directions if i[0] == 'down ')
result = horizontal*(down-up)
print(result)


#final_position = (up-down)*horizontal
#print(final_position)

