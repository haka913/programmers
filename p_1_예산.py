d = [1, 3, 2, 5, 4]
budget = 9


def solution(d, budget):
    d.sort()
    answer = 0

    sum = 0
    for i in d:
        if sum + i <= budget:
            sum += i
            answer += 1

        else:
            break

    return answer

print(solution(d,budget))