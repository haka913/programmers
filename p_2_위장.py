def solution(clothes):
    dic = {}
    for clothe in clothes:
        dic[clothe[1]] = dic.get(clothe[1], []) + [clothe[0]]

    answer = 1
    for i in dic.values():
        answer *= len(i)+1
    answer -=1
    return answer


print(solution(clothes=[['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
