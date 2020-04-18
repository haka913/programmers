def solution(weight):
    scale_min = 1
    weight.sort()
    for i in weight:
        if scale_min < i:
            break
        scale_min += i
    return scale_min

print(solution(weight=[3, 1, 6, 2, 7, 30, 1]))