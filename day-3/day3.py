"""
param
1) power consumption = gamma rate * epsilon rate
gamma rate = most common bit in the corresponding position
epsilon rate = least common bit in the corresponding position

2) life support rating = oxygen generator rating * CO2 scrubber rating
Consider first bit:
    - Keep only numbers selected by the bit criteria for the type rating value for which you are searching.
      Discard numbers which do not match the bit criteria.
    - If you only have one number left, stop; this is the rating value for which you are searching.
    - Otherwise, repeat the process, considering the next bit to the right.

Bit criteria depends on which type of rating value you want to find:
    - Oxygen generator rating:
        determine the most common value in the current bit position, and keep only numbers with that bit
        in that position. If they are equally as likely, keep a 1.
    - CO2 scrubber rating:
        determine the least common value in the current bit position, and keep only numbers with that bit 
        in that position. If they are equally as likely, keep a 0.
"""



data = open('input.txt', 'r', encoding='utf-8').read().splitlines()

""" pt 1 """
def rate():
    g = "" # gamma value (most common)
    e = "" # epsilon value (least common)
    zeros=ones=0
    for i in range(len(data[0])):
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
        print('zeros: ' + str(zeros) + ' ones: ' + str(ones))
        zeros=ones=0
    return (int(g, 2)*int(e, 2))



""" pt 2 """
def oxy():
    temp_arr = [i for i in data]
    for i in range(len(temp_arr[0])):
        print(temp_arr)
        z, o = bit_freq(i, temp_arr)
        if z == o:
            oxy_bit = '1'
        else:
            oxy_bit = '0' if z > o else '1'
        temp_arr = find_and_remove(temp_arr, i, oxy_bit)
        if len(temp_arr) == 1:
            break
    return int(temp_arr[0], 2)


def co2():
    temp_arr = [i for i in data]
    for i in range(len(temp_arr[0])):
        print(temp_arr)
        z, o = bit_freq(i, temp_arr)
        if z == o:
            oxy_bit = '0'
        else:
            oxy_bit = '1' if z > o else '0'
        temp_arr = find_and_remove(temp_arr, i, oxy_bit)
        if len(temp_arr) == 1:
            break
    return int(temp_arr[0], 2)


def find_and_remove(arr, index, bit):
    new_arr = [i for i in arr if i[index] == bit]
    return new_arr

   
def bit_freq(column, arr):
    z = sum(1 for row in arr if row[column] == '0')
    o = len(arr) - z
    return (z, o)


if __name__ == '__main__':
    rate_num = rate()
    most = oxy()
    least = co2()
    lfsr = most*least
    print('most: ' + str(most))
    print('least: ' + str(least))
    print('life-support-rating: ' + str(lfsr))
