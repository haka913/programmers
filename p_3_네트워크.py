def dfs(computers, visited, start):
    stack = [start]
    while stack:
        m = stack.pop()
        if visited[m] ==0:
            visited[m] = 1
        for i in range(len(computers)):
            if computers[m][i] == 1 and visited[i]==0:
                stack.append(i)


def solution(n, computers):
    answer = 0
    visited = [0]*n
    i =0
    while 0 in visited:
        if visited[i]==0:
            dfs(computers,visited,i)
            answer+=1
        i+=1

    return answer


print(solution(n=3, computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# def solution(n, computers):
#     def BFS(node, visit):
#         que = [node]
#         visit[node] = 1
#         while que:
#             v = que.pop(0)
#             for i in range(n):
#                 if computers[v][i] == 1 and visit[i] == 0:
#                     visit[i] = 1
#                     que.append(i)
#         return visit
#     visit = [0 for i in range(n)]
#     answer = 0
#     for i in range(n):
#         try:
#             visit = BFS(visit.index(0), visit)
#             answer += 1
#         except:
#             break
#     return answer