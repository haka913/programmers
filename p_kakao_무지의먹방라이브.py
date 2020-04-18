food_times = [3, 1, 2]
k = 5


def solution(food_times, k):
    timeIdx = [[time,idx] for idx, time in enumerate(food_times)]
    size = len(food_times)
    timeIdx.sort()
    print(timeIdx)
    answer = 0

    return answer


print(solution(food_times, k))
#Todo: 풀기