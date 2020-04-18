m, n = 4, 3
puddles = [[2, 2]]
MOD = 1000000007


def solution(m, n, puddles):
    MOD = 1000000007
    root = [[0] * (m+1) for i in range(n+1)]
    dp = [[0] * (m+1) for i in range(n+1)]
    for x in puddles:
        root[x[1]][x[0]] = -1
        # print(x[0],x[1])
    dp[1][0] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if root[i][j] == -1:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
    return dp[n][m]


print(solution(m, n, puddles))


# def solution(m, n, puddles):
#     answer = 0
#     info = dict([((2, 1), 1), ((1, 2), 1)])
#     for puddle in puddles:
#         info[tuple(puddle)] = 0
#
#     def func(m, n):
#         if m < 1 or n < 1:
#             return 0
#         if (m, n) in info:
#             return info[(m, n)]
#         return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))
#     return  func(m, n) % 1000000007