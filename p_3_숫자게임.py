def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    a = len(A) - 1
    b = len(B) - 1
    while a >= 0:
        if B[b] > A[a]:
            b -= 1
            answer += 1
        a -= 1
    return answer


print(solution(A=[5, 1, 3, 7], B=[2, 2, 6, 8]))
