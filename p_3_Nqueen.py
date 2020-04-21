def checkCollision(row, board):
    for i in range(row):
        if board[i] == board[row] or abs(board[i] - board[row]) == row - i:
            return False
    return True


def nqueen(row, board, n):
    if row == n:
        return 1

    count = 0
    for i in range(n):
        board[row] = i
        if checkCollision(row, board):
            count += nqueen(row + 1, board, n)
    return count

def solution(n):
    board = [0] * n
    answer = nqueen(0, board, n)
    return answer


print(solution(n=4))
