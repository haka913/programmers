import re

def solution(dartResult):
    re1 = re.compile("(\d{1,2})([SDT])([*#])?")
    list1 = re1.findall(dartResult)
    answer = []
    for idx, dx in enumerate(list1):
        point = dx[0]
        bonus = dx[1]
        option = dx[2]

        if bonus == 'S':
            bonus = 1
        elif bonus == 'D':
            bonus = 2
        elif bonus == 'T':
            bonus = 3

        if option == '*':
            if idx == 0:
                answer.append(int(point) ** bonus * 2)
            else:
                answer[-1] *= 2
                answer.append(int(point) ** bonus * 2)
        elif option == '#':
            answer.append(int(point) ** bonus * -1)
        else:
            answer.append(int(point) ** bonus)

    return sum(answer)


print(solution(dartResult="1D2S#10S"))
# print(solution(dartResult="1S*2T*3S"))
