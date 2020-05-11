from collections import deque


def bfs(maps, y, x, cnt):
    # UP,DOWN,LEFT,RIGHT
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    q = deque()
    q.append((y, x, cnt))
    while q:
        cy, cx, ccnt = q.popleft()
        maps[y][x] = 0
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if ny == len(maps) - 1 and nx == len(maps[0]) - 1:
                return ccnt + 1
            elif 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == 1:
                maps[ny][nx] = 0
                q.append((ny, nx, ccnt + 1))
    return -1

def solution(maps):
    answer = bfs(maps, 0, 0, 1)
    return answer


print(solution(maps=[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution(maps=[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
