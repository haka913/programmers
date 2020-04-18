
from collections import Counter
def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    split_str1 = []
    split_str2 = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            split_str1.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            split_str2.append(str2[i:i + 2])

    if not split_str1 and not split_str2:
        return 65536
    intersection_set = list((Counter(split_str1)&Counter(split_str2)).elements())
    if len(intersection_set)==0:
        return 0

    len_union = len(split_str1)+len(split_str2)-len(intersection_set)

    answer = int(len(intersection_set) / len_union * 65536)
    return answer


print(solution(str1="FRANCE", str2="french"))  # 16384
print(solution(str1="handshake", str2="shake hands")) # 65536
print(solution(str1="aa1+aa2", str2="AAAA12")) # 43690
print(solution(str1="E=M*C^2", str2="e=m*c^2")) # 65536
