A = [1, 4, 2]
B = [5, 4, 4]


def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    return sum([a*b for a,b in zip(A,B)])


print(solution(A,B))