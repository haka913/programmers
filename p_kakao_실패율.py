def solution(N, stages):
    stages.sort()
    # print(stages)

    result = {}
    people = len(stages)
    for i in range(1 ,N+1):
        if people!=0:
            cnt = stages.count(i)
            result[i] = cnt/people
            people -=cnt
        else:
            result[i]=0
    # print(result)
    return sorted(result, key=lambda x: result[x], reverse=True)



print(solution(N=5,stages=[2, 1, 2, 6, 2, 4, 3, 3]))