# boj 3079

def solution(n, times):
    times.sort()
    answer = 0
    start, end = 1, times[-1] * n
    while start <= end:
        mid = (start + end) // 2
        people = 0
        for i in times:
            people += mid // i
            if people >= n:
                break

        if people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


print(solution(n=6, times=[7, 10]))
