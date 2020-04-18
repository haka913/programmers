n = 4
works = [4, 3, 3]


def solution(n, works):
    if n>=sum(works):
        return 0
    works.sort()
    for i in range(n):
        works.sort()
        works[-1]-=1

    answer = sum([i**2 for i in works])
    return answer


print(solution(n, works))

# todo 야근지수