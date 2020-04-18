N = 5


def solution(N):
    dp = [1, 1, 2]
    for i in range(3, N):
        dp.append(dp[i - 1] + dp[i - 2])

    # print(dp)
    answer = dp[N - 1] * 4 + dp[N - 2] * 2
    return answer


print(solution(N))
