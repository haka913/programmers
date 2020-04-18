# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

# build_frame의 원소는 [x, y, a, b]형태입니다.
# x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
# a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
# 벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
# 바닥에 보를 설치 하는 경우는 없습니다.

# 최종 구조물의 상태는 아래 규칙에 맞춰 return 해주세요.
# return 하는 배열은 가로(열) 길이가 3인 2차원 배열로, 각 구조물의 좌표를 담고있어야 합니다.
# return 하는 배열의 원소는 [x, y, a] 형식입니다.
# x, y는 기둥, 보의 교차점 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
# 기둥, 보는 교차점 좌표를 기준으로 오른쪽, 또는 위쪽 방향으로 설치되어 있음을 나타냅니다.
# a는 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# return 하는 배열은 x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬해주세요.
# x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.
def solution(n, build_frame):
    dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    build_col = [[0] * (n + 2) for _ in range(n + 2)]  # 기둥
    build_beam = [[0] * (n + 2) for _ in range(n + 2)]  # 보

    def check_beam(y, x):
        return build_col[y - 1][x] or build_col[y - 1][x + 1] or (build_beam[y][x - 1] and build_beam[y][x + 1])

    def check_col(y, x):
        return y == 0 or build_col[y - 1][x] or build_beam[y][x] or build_beam[y][x - 1]

    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0:  # 삭제 (조건 불만족시 무시)
            if a == 0:  # 기둥
                build_col[y][x] = 0
                for i in range(9):
                    ny, nx = y + dy[i], x + dx[i]
                    if nx >= 0 and ny >= 0:
                        if build_col[ny][nx] == 1:
                            if not check_col(ny, nx):
                                build_col[y][x] = 1
                                break
                        if build_beam[ny][nx] == 1:
                            if not check_beam(ny, nx):
                                build_col[y][x] = 1
                                break
            elif a == 1:  # 보
                build_beam[y][x] = 0
                for i in range(9):
                    ny, nx = y + dy[i], x + dx[i]
                    if nx >= 0 and ny >= 0:
                        if build_col[ny][nx] == 1:
                            if not check_col(y, x):
                                build_beam[y][x] = 1
                                break
                        if build_beam[ny][nx] == 1:
                            if not check_beam(ny, nx):
                                build_beam[y][x] = 1
                                break
        elif b == 1:  # 설치
            if a == 0:  # 기둥
                if check_col(y, x):
                    build_col[y][x] = 1
            elif a == 1:  # 보
                if check_beam(y, x):
                    build_beam[y][x] = 1

    # for i in build_col:
    #     print(*i)
    # print()
    # for i in build_beam:
    #     print(*i)

    # for idx_i, val_i in enumerate(build_col):
    #     for idx_j, val_j in enumerate(val_i):
    #         if val_j:
    #             answer.append([idx_j, idx_i, 0])
    # for idx_i, val_i in enumerate(build_beam):
    #     for idx_j, val_j in enumerate(val_i):
    #         if val_j:
    #             answer.append([idx_j, idx_i, 1])
    for y in range(n + 2):
        for x in range(n + 2):
            if build_col[y][x]:
                answer.append([x, y, 0])
            if build_beam[y][x]:
                answer.append([x, y, 1])
    answer.sort()
    return answer


# print(solution(n=5, build_frame=[[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1],
#                                  [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(n=5, build_frame=[[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1],
                                 [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
