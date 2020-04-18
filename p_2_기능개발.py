import math
import itertools

progresses = [93, 30, 55]
speeds = [1, 30, 5]


def solution(progresses, speeds):
    answer = []
    workDone = []
    for i, j in zip(progresses, speeds):
        workDone.append(math.ceil((100 - i) / j))

    # print(workDone)
    for idx in range(len(workDone)):
        if idx == len(workDone) - 1:
            break
        if workDone[idx] > workDone[idx + 1]:
            workDone[idx + 1] = workDone[idx]
    # print(workDone)
    cnt = 0
    tmp = workDone[0]
    while workDone:
        if tmp == workDone[0]:
            # print("if tmp is %d"%tmp)
            cnt += 1
            del workDone[0]
        else:
            tmp = workDone[0]
            # print("else tmp is %d" % tmp)
            answer.append(cnt)
            cnt = 0
    answer.append(cnt)

    # print(answer)
    return answer


print(solution(progresses, speeds))
