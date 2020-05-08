def checkDir(x, y):
    if x > 5 or y > 5 or x < -5 or y < -5:
        return False
    return True


def solution(dirs):
    dx = [0, 0, -1, 1]  # up, down, left, right
    dy = [1, -1, 0, 0]
    dir = ['U', 'D', 'L', 'R']
    res = set()
    curX, curY = 0, 0
    answer = 0
    for d in dirs:
        i = dir.index(d)
        nx, ny = curX + dx[i], curY + dy[i]
        if checkDir(nx, ny):
            if (curX, curY, nx, ny) not in res:
                res.add((curX, curY, nx, ny))
                res.add((nx, ny, curX, curY))
                answer += 1
        else:
            continue
        curX, curY = nx, ny
    return answer


print(solution(dirs='ULURRDLLU'))
print(solution(dirs='LULLLLLLU'))
