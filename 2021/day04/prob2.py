import sys

class Board(object):


    def __init__(self):
        self.rows = []
        self.marked = set()
        self.board_len = 5
        self.won = False

    def add_row(self, row):
        self.rows.append(row)

    def mark(self, called_num):
        for row in range(self.board_len):
            for i, num in enumerate(self.rows[row]):
                if num == called_num:
                    self.add_mark((row, i))
                    if self.check_for_win(row, i):
                        self.won = True

    def add_mark(self, tup):
        self.marked.add(tup)

    def check_for_win(self, row, column):
        marked_count = 0
        for i in range(self.board_len):
            if (row, i) not in self.marked:
                break
            else:
                marked_count += 1
        if marked_count == 5:
            return True
        for i in range(self.board_len):
            if (i, column) not in self.marked:
                return False
        return True

    def calculate(self, called_num):
        board_sum = 0
        for row in range(self.board_len):
            for i, num in enumerate(self.rows[row]):
                if (row, i) not in self.marked:
                    board_sum += int(num)
        return board_sum * int(called_num)

    def __repr__(self):
        return repr(self.rows)

boards = []
in_board = False

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        if ',' in line:
            bingo_nums = line.split(',')
        elif line == '':
            in_board = False
        else:
            if not in_board:
                cur_board = Board()
                in_board = True
            row = line.split()
            cur_board.add_row(row)
            if len(cur_board.rows) == 5:
                boards.append(cur_board)

current_score = None
for num in bingo_nums:
    for board in boards:
        if not board.won:
            board.mark(num)
            if board.won:
                current_score = board.calculate(num)

print(current_score)
