from string import ascii_uppercase


def solution(msg):
    dic = list(ascii_uppercase)
    answer = []
    while msg:
        cur = ''
        idx = 0
        for i in range(1, len(msg) + 1):
            if msg[:i] in dic:
                cur = msg[:i]
                idx = i
        msg = msg[idx:]
        if msg:
            dic.append(cur + msg[0])
        answer.append(dic.index(cur) + 1)

    return answer


print(solution(msg='KAKAO'))
