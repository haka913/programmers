board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]


# 최고 큰 정 사각형 한변 기록이 cnt 이라고 하고
# 보드의 점이 1이면 (x-1, y-1), (x, y-1), (x-1, y) 세점이 1인지 확인한다.

# 세점이 0 이면
# 현재 위치와 cnt과 비교하여 크면 cnt 갱신

# 세점이 1 이상이면 세점중 가장 작은 수 + 1 을 현재 위치에 대입
# 현재 위치와 cnt과 비교하여 크면 cnt 갱신

# 최종 cnt을 제곱하면 가장 큰 정사각형의 크기를 구할수 있다.

def solution(board):
    cnt = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            # print(board[row][col], end=" ")
            if board[row][col]:
                isRec = min(board[row - 1][col - 1], board[row - 1][col], board[row][col - 1])
                if isRec and row and col:
                    board[row][col] = isRec + 1
                if board[row][col] > cnt:
                    cnt = board[row][col]
    answer = cnt ** 2
    return answer


print(solution(board))

# # dp로 풀기
# def findLargestSquare(board):
#     answer = 1
#     res = [[1 if x=='O' else 0 for x in y] for y in board]
#     for y in range(len(board)):
#         for x in range(len(board[y])):
#             if board[y][x] == 'O':
#                 res[y][x] = min(res[y-1][x], res[y-1][x-1], res[y][x-1]) + 1
#                 if res[y][x] > answer: answer = res[y][x]
#
#     return answer ** 2
