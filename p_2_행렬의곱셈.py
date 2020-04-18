import numpy as np

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]


def solution(arr1, arr2):
    answer = [[]]

    matmul = [[0]*len(arr2[0]) for i in range(len(arr1))]
    print(matmul)
    for i in range(len(matmul)):
        for j in range(len(matmul[i])):
            for k in range(len(arr1[i])):
                matmul[i][j] += arr1[i][k]*arr2[k][j]

    print(matmul)
    answer = np.matmul(arr1,arr2).tolist()
    return answer


print(solution(arr1, arr2))


# def productMatrix(A, B):
#     return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]