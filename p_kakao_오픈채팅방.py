record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]


def solution(record):
    user = dict()
    chat = []
    for i in record:
        lis1 = i.split(' ')
        # print(lis1)
        if lis1[0] == 'Enter':
            user[lis1[1]] = lis1[2]
            chat.append([lis1[1], '님이 들어왔습니다.'])
        elif lis1[0] == 'Leave':
            chat.append([lis1[1], '님이 나갔습니다.'])
        elif lis1[0] == 'Change':
            user[lis1[1]] = lis1[2]

    print("chat is")
    print(chat)
    print("user is")
    print(user)
    answer = []
    for c in chat:
        answer.append(user[c[0]] + c[1])
    return answer


print(solution(record))
