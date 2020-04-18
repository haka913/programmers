def solution(brown, red):
    answer = []
    for i in range(1, int(red**0.5) + 1):
        if red % i == 0:
            w, h = max(red // i, i), min(red // i, i)
            if 2 * w + 2 * h + 4 == brown:
                answer.append(w + 2)
                answer.append(h + 2)
                break
    return answer


print(solution(brown=8, red=1))

# def solution2(brown, red):
#     for i in range(1, int(red**(1/2))+1):
#         if red % i == 0:
#             if 2*(i + red//i) == brown-4:
#                 return [red//i+2, i+2]