import re
import ast

def solution(s):
    s = s.replace("{",'[').replace("}",']')#.replace(",", ' ')

    #string list를 list로 바꾸는 방법
    # https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/
    lis = ast.literal_eval(s)

    sorted_list = sorted(lis, key=len)

    answer = []
    for i in sorted_list:
        # print(i)
        for elem in i:
            if(elem not in answer):
                answer.append(elem)


    return answer


# print(solution(s="{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# print(solution(s="{{20,111},{111}}"))
# print(solution(s="{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution(s="{{4,2,3},{3},{2,3,4,1},{2,3}}"))
