data = open('input.txt', 'r', encoding='utf-8').read().splitlines()
rand_nums, board_nums = data[0].split(','), [i.split() for i in data[1:] if i != '']

class Boards:
    def __init__(self, arr):
        assert(len(arr[0])%5 == 0 and len(arr)%5 == 0), "that ain't no list of bingo boards, bud!"
        self.arr = arr
        self.board_list = self.arrange()

    def board_count(self):
        return int(len(self.arr)/5)

    def arrange(self):
        board_list = [0]*self.board_count()
        s = 0
        for i in range(len(board_list)):
            board_list[i] = self.arr[s:s+5]
            s+=5
        return board_list

    def print_boards(self):
        for i in self.board_list:
            for j in i:
                print(j)
            print('\n')

    def check_columns(self, board):
        for column in range(5):
            x = 0
            for row in board:
                if row[column] == 'X':
                    x += 1
            if x == 5:
                return board

    def check_rows(self, board):
        for row in board:
            x = 0 
            for column in row:
                if column == 'X':
                    x += 1
            if x == 5:
                return board


    def check_boards(self):
        for board in self.board_list:
            c, r = self.check_columns(board), self.check_rows(board)
            if c != None:
                return c
            if r != None:
                return r

    def remove_board(self, board):
        self.board_list.remove(board)

    def input_nums(self, num):
        for i in self.arr:
            for j in range(5):
                if i[j] == num:
                    i[j] = 'X'
            winner = self.check_boards()
            if winner != None:
                return (winner, num)

    def get_loser(self, num):
        for i in self.arr:
            for j in range(5):
                if i[j] == num:
                    i[j] = 'X'
            winner = self.check_boards()
            # print(num)
            # self.print_boards()
            if winner != None and len(self.board_list) != 1:
                self.remove_board(winner)
            elif winner != None and len(self.board_list) == 1:
                loser = self.board_list[0]
                return (loser, num)
                break

def get_score(b):
    not_x, board, multiple = 0, b[0], b[1]
    for row in board:
        for i in row:
            if i != 'X':
                not_x += int(i)
    print('sum: ' + str(not_x))
    return int(multiple) * not_x


boards = Boards(board_nums)
"""
for inputs in rand_nums:
    print(inputs)
    winner = boards.input_nums(inputs)
    if winner != None:
        print(winner)
        break
"""
for inputs in rand_nums:
    loser = boards.get_loser(inputs)
    if loser != None:
        break


print('score: ' + str(get_score(loser)))
