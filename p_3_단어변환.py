from collections import deque


def compareWord(str1, str2):
    cnt = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            cnt += 1
    if cnt == len(str1) - 1:
        return True
    else:
        return False


def bfs(start, end, words, visited):
    q = deque()
    q.append([start, 0])
    while q:
        word, cnt = q.popleft()
        for i in range(len(words)):
            if compareWord(word, words[i]):
                if words[i] == end:
                    return cnt + 1
                if not visited[i]:
                    q.append([words[i], cnt + 1])
                    visited[i] = True
    return 0


def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [False] * len(words)
    answer = bfs(begin, target, words, visited)

    return answer


print(solution(begin="hit", target="cog", words=['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
