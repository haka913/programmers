n = 5
lost = [2,4,5]
reserve = [1,4]
def solution(n, lost, reserve):
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    answer = n - len(lost)
    return answer

def solution(n, lost, reserve):
    for l in lost[:]:
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
    for l in lost[:]:
        if l > 1:
            if l-1 in reserve:
                lost.remove(l)
                reserve.remove(l-1)
    for l in lost[:]:
        if l < n:
            if l+1 in reserve:
                lost.remove(l)
                reserve.remove(l+1)
    return n - len(lost)
# def solution(n, lost, reserve):
#     reserve_1 = [i for i in reserve if i not in lost]
#     lost_1 = [i for i in lost if i not in reserve]
#
#     for i in reserve_1:
#         if i-1 in lost_1:
#             lost_1.remove(i-1)
#         elif i+1 in lost_1:
#             lost_1.remove(i+1)
#
#     return n-len(lost_1)


print(solution(n,lost,reserve))
