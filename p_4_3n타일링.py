def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3
    mod = 1000000007
    sum = 0
    for i in range(2, n + 1, 2):
        dp[i] = dp[i-2]*3+sum*2
        sum += dp[i-2]
        # for j in range(4,i+1,2):
        #     dp[i] += dp[i-j]*2

    answer = dp[n]%mod
    return answer


print(solution(n=4))
