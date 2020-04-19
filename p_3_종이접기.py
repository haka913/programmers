def solution(n):
    s = [0]

    for i in range(1, n):
        fold = s[::-1]
        for i in range(len(fold)):
            if fold[i]:
                fold[i] = 0
            else:
                fold[i] = 1
        s.append(0)
        s += fold

    return s


print(solution(n=3))

# def solution(n):
#     fold = 0
#     arr = [fold]
#
#     for i in range(n - 1):
#         arr = arr + [fold] + [bit ^ 1 for bit in arr[::-1]]
#     return arr
