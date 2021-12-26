"""
- down X increases your aim by X units.
- up X decreases your aim by X units.
- forward X does two things:
    - It increases your horizontal position by X units.
    - It increases your depth by your aim multiplied by X.
"""
data = open('input.txt', 'r', encoding='utf-8').read().splitlines()
directions = [(i[:-1], int(i[-1])) for i in data]

aim, depth, horizontal = 0, 0, 0
for i in directions:
    if i[0] == 'down ':
        aim += i[1]
    if i[0] == 'up ':
        aim -= i[1]
    if i[0] == 'forward ':
        horizontal += i[1]
        depth += (aim*i[1])

print('horizontal: ' + str(horizontal))
print('depth: ' + str(depth))
print('final: ' + str(horizontal*depth))
