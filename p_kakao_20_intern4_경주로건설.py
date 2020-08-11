# 2020 카카오 인턴십4 경주로 건설
# https://programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

# up, left, down, right
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def bfs(board):
    answer = 600 * 25 * 25
    n = len(board)
    q = deque()
    # cost, dir
    visitCost = [[[600 * 25 * 25, -2]] * n for _ in range(n)]
    # y,x,cost,dir
    q.append((0, 0, 0, -1))
    while q:
        y, x, cost, dir = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if -1 < nx < n and -1 < ny < n and not board[ny][nx]:
                ncost = cost
                if dir == -1:
                    ncost += 100
                elif (dir - i) % 2 == 1:
                    ncost += 600
                else:
                    ncost += 100

                if ny == n - 1 and nx == n - 1:
                    answer = min(answer, ncost)
                # cost 같아도 추가해야 같은 방향이 넣어짐
                elif visitCost[ny][nx][0] >= ncost or visitCost[ny][nx][1] == -2:
                    visitCost[ny][nx] = [ncost, i]
                    q.append((ny, nx, ncost, i))

    return answer


def solution(board):
    answer = bfs(board)
    # print("answer is ", answer)
    return answer


if __name__ == '__main__':
    print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))  # 900
    print(solution(
        [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0]]))  # 3800
    print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))  # 2100
    print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0]]))  # 3200
