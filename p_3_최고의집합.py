def solution(n, s):
    if n > s:
        return [-1]
    else:
        portion, remain = divmod(s, n)
        answer = [portion] * n
        for i in range(remain):
            answer[i] += 1
        answer.sort()
        return answer


print(solution(n=2, s=9))
