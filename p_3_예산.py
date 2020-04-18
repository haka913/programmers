def solution(budgets, M):
    lo = 0
    hi = max(budgets)
    answer = 0
    budgets.sort()
    while hi >= lo:
        mid = (lo + hi) // 2
        result = 0
        for i in budgets:
            if mid > i:
                result += i
            else:
                result += mid
        if result > M:
            hi = mid - 1
        else:
            if result >= answer:
                answer = mid
            lo = mid + 1

    return answer


print(solution(budgets=[120, 110, 140, 150], M=485))

# def solution(budgets, M):
#     lim=max(budgets)
#
#     while True:
#         if sum(budgets)<M:
#             answer=max(budgets)
#             break
#
#         budgets=list(map(lambda x: x if x<=lim else lim,budgets))
#         lim=lim-1
#
#     return answer
