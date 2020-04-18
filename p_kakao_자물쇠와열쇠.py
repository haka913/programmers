import copy


def solution(key, lock):
    m = len(key[0])
    n = len(lock[0])

    def check_unlocked(arr):
        for i in range(n, n + n):
            for j in range(n, n + n):
                if arr[i][j] != 1:
                    return False
        return True

    # 4방향에 대한 key의 배열위치 값 저장
    keyr = [[[0] * m for _ in range(m)] for _ in range(4)]
    for i in range(m):
        for j in range(m):
            keyr[0][i][j] = key[i][j]

    for r in range(1, 4):
        for i in range(m):
            for j in range(m):
                keyr[r][i][j] = keyr[r - 1][m - 1 - j][i]

    # lock을 새로운 배열 중앙에 놓는다
    new_lock = [[0] * n * 3 for _ in range(n * 3)]

    for i in range(0, n):
        for j in range(0, n):
            new_lock[i + n][j + n] = lock[i][j]

    tmp_lock = copy.deepcopy(new_lock)

    def lock_copy(newarr, tmparr):
        for i in range(n, n + n):
            for j in range(n, n + n):
                newarr[i][j] = tmparr[i][j]

    for r in range(4):
        for x in range(0, n + n):
            for y in range(0, n + n):
                for i in range(m):
                    for j in range(m):
                        new_lock[i + x][j + y] += keyr[r][i][j]

                if check_unlocked(new_lock):
                    return True
                else:
                    lock_copy(new_lock, tmp_lock)

    return False


print(solution(key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]], lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
