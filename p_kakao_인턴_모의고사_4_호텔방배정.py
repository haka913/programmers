
import sys
sys.setrecursionlimit(100000)

def findRoom(n,room):
    if n not in room:
        room[n] = n+1
        return n
    m = findRoom(room[n],room)
    room[n] = m+1
    return m


def solution(k, room_number):
    answer = []
    rooms = dict()
    for room in room_number:
        emptyroom = findRoom(room, rooms)
        answer.append(emptyroom)
    return answer

# 효율성 테스트 실패

print(solution(k=10, room_number=[1, 3, 4, 1, 3, 1]))
