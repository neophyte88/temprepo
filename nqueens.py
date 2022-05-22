N = 8

def printsolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def is_safe(row, col, slashcode, backslashcode, rowlookup, slashcodelookup, backslashcodelookup):
            if(slashcodelookup[slashcode[row][col]] or backslashcodelookup[backslashcode[row][col]] or rowlookup[row]):
                return False
            return True

def solve_nqueens_util(board, col, slashcode, backslashcode, rowlookup, slashcodelookup, backslashcodelookup):
    if (col >= N):
        return True

    for i in range(N):
        if(is_safe(i, col, slashcode, backslashcode, rowlookup, slashcodelookup, backslashcodelookup)):
            board[i][col] = 1
            rowlookup[i] = True
            slashcodelookup[slashcode[i][col]] = True
            backslashcodelookup[backslashcode[i][col]] = True

            if(solve_nqueens_util(board, col+1, slashcode, backslashcode, rowlookup, slashcodelookup, backslashcodelookup)):
                return True

            board[i][col] = 0
            rowlookup[i] = False
            slashcodelookup[slashcode[i][col]] = False
            backslashcodelookup[backslashcode[i][col]] = False
    return False
def solve():
    board = [[0 for i in range(N)] for j in range(N)]

    slashcode = [[0 for i in range(N)] for j in range(N)]

    backslashcode = [[0 for i in range(N)] for j in range(N)]

    rowlookup = [False] * N

    x = 2 * N - 1

    slashcodelookup = [False] * x
    backslashcodelookup = [False] * x

    for rr in range(N):
        for cc in range(N):
            slashcode[rr][cc] = rr + cc
            backslashcode[rr][cc] = rr - cc + 7

    if(solve_nqueens_util(board, 0, slashcode, backslashcode, rowlookup, slashcodelookup, backslashcodelookup) == False):
        print("solution does not exist")
        return False

    printsolution(board)
    return True

solve()
