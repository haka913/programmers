import math

def solution(n, k):
    person = [i for i in range(1, n + 1)]
    print(person)
    answer = []
    while n > 0:
        n -= 1
        q, r = divmod(k, math.factorial(n))
        if r == 0:
            q -= 1
        answer.append(person[q])
        person.remove(person[q])
        k = r
    return answer


print(solution(n=3, k=5))
