# 입력 블록 A-Z로 주어짐 지문과 헷갈리지 않기
def solution(m, n, board):
    # for i in board:
    #     print(*i)

    while True:
        board = [list(i) for i in board]

        idxlist = []
        for i in range(len(board) - 1):
            for j in range(len(board[0]) - 1):
                if board[i][j] !='#' and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 1][j + 1]:
                    idxlist.append([i, j])

        if idxlist:
            for i, j in idxlist:
                board[i][j] = '#'
                board[i][j+1] = '#'
                board[i+1][j] = '#'
                board[i+1][j+1] = '#'

            for j in range(len(board[0])):
                tmp =''
                for i in range(len(board)):
                    tmp += board[i][j]
                    tmp = tmp.replace('#','')
                    tmp = tmp.rjust(len(board),'#')
                for i in range(len(tmp)):
                    board[i][j] = tmp[i]

        else:
            break
        idxlist.clear()

    answer = 0
    for i in board:
        answer += i.count('#')
    return answer


# print(solution(m=6, n=6, board=['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))
print(solution(m=4, n=5, board=['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
