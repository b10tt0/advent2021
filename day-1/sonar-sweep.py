def load_data():
    data = open('input.txt', 'r', encoding='utf-8').read().split()
    depths = [int(row) for row in data]
    return depths

def increase_counter():
    data = load_data()
    result = sum(x > y for x, y in zip(data[1:], data))
    print(result)


def increase_counter_3():
    data = load_data()
    result = sum(x > y for x, y in zip(data[3:], data))
    print(result)


""" another way to do the same thing as increase_counter_3()... sort of """
def group_three_sum(i, arr):
    return int(arr[i] + arr[i+1] + arr[i+2])


if __name__ == '__main__':
    increase_counter()
    increase_counter_3()
