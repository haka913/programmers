from collections import deque


def bfs(start, nodes, visited):
    count = 0
    q = deque([[start, count]])
    while q:
        node = q.popleft()
        v, count = node[0], node[1]
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in nodes[v]:
                q.append([e, count])


def solution(n, edge):
    visited = [-1] * (n + 1)
    nodes = [[] for _ in range(n + 1)]
    for e in edge:
        x, y = e[0], e[1]
        nodes[x].append(y)
        nodes[y].append(x)

    bfs(1, nodes, visited)
    answer = visited.count(max(visited))
    return answer


print(solution(n=6, edge=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
