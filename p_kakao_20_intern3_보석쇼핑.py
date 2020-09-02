# 2020 카카오 인턴십3 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258

from collections import defaultdict


def solution(gems):
    gem_set = set(gems)
    gem_length = len(gem_set)
    # default int(0)으로 set
    # defaultdict(lambda:0)
    gem_dict = defaultdict(int)
    gem_dict[gems[0]] = 1

    answer = [0, len(gems)]
    start, end = 0, 0
    while start < len(gems) and end < len(gems):
        if len(gem_dict) == gem_length:
            if answer[1] - answer[0] > end - start:
                answer = [start + 1, end + 1]

            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                gem_dict.pop(gems[start])
                # del gem_dict[gems[start]]
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            gem_dict[gems[end]] += 1
            # if gems[end] in gem_dict:
            #     gem_dict[gems[end]] +=1
            # else:
            #     gem_dict[gems[end]] =1
    return answer


if __name__ == '__main__':
    print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))  # [3, 7]
    print(solution(["AA", "AB", "AC", "AA", "AC"]))  # [1, 3]
    print(solution(["XYZ", "XYZ", "XYZ"]))  # [1, 1]
    print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))  # [1, 5]
