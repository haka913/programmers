def solution(n):
    dp = [1, 2]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    answer = dp[n-1]
    # print(dp)
    return answer

print(solution(4))
