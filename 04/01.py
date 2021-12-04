# each time i find a number ill put star in it's place

def check_board(board):
    is_win = False
    for i in board:
        has_nums = False
        for j in i:
            if j != '*':
                has_nums = True
        if not(has_nums):
            return True

    for j in range(5):
        has_nums = False
        for k in range(5):
            if board[k][j] != '*':
                has_nums = True
        if not(has_nums):
            return True

    return False


with open("nums.txt", "r") as nums, open("input.txt", "r") as f:
    nums = nums.read().split(",")
    f = f.read().split("\n\n")
    boards = []
    for i in f:
        i = i.split("\n")
        a = []
        for j in i:
            j.split(" ")
            a.append(j.split())
        boards.append(a)
    for i in nums:
        for j in range(len(boards)):
            for k in range(5):
                for l in range(5):
                    boards[j][k][l] = '*' if boards[j][k][l] == i else boards[j][k][l]

        for j in range(len(boards)):
            print(i)
            print(boards[j])
            print(check_board(boards[j]))
