triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def soltuion(triagnle):
    for i in range(len(triangle) - 1, 0, -1):
        for j in range(i):
            triangle[i - 1][j] += max(triangle[i][j], triangle[i][j + 1])

    answer = triangle[0][0]
    return answer


print(soltuion(triangle))

# def solution(triangle):
#     for i in range(1,len(triangle)):
#         for j in range(i+1):
#             if j==0:
#                 triangle[i][j]+=triangle[i-1][j]
#             elif j==i:
#                 triangle[i][j]+=triangle[i-1][j-1]
#             else:
#                 triangle[i][j]+=max(triangle[i-1][j],triangle[i-1][j-1])
#     return max(triangle[-1])
