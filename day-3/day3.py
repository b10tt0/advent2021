"""
param
1) power consumption = gamma rate * epsilon rate
gamma rate = most common bit in the corresponding position
epsilon rate = least common bit in the corresponding position
"""

data = open('input.txt', 'r', encoding='utf-8').read().splitlines()

def rate():
    g = "" # gamma value (most common)
    e = "" # epsilon value (least common)
    zeros, ones = 0, 0
    for i in range(0, len(data[0])):
        for j in  data:
            if j[i] == '0':
                zeros += 1
            else: 
                ones += 1
        if zeros > ones:
            g += '0'
            e += '1'
        else:
            g += '1'
            e += '0'
        zeros, ones = 0, 0
    return (int(g, 2)*int(e, 2))


if __name__ == '__main__':
    rate_num = rate()
    print(rate_num)
