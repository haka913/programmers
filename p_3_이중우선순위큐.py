def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def divOp(s):
    if is_number(s):
        return int(s)
    else:
        return s


def solution(operations):
    q = []
    answer = []
    for i in operations:
        op, n = map(divOp, i.split())
        if op == 'I':
            q.append(n)
        elif op == 'D':
            if q:
                if n == 1:
                    q.remove(max(q))
                elif n == -1:
                    q.remove(min(q))

    if not q:
        answer = [0, 0]
    else:
        answer = [max(q), min(q)]

    return answer


import heapq
def solution1(operations):
    heap = []
    for oper in operations:
        op, n = oper.split(' ')
        if op == 'I':
            heapq.heappush(heap, int(n))
        elif op=='D':
            if heap:
                if n=='1':
                    heap.remove(max(heap))
                else:
                    heapq.heappop(heap)

    if not heap:
        return [0,0]
    return [max(heap), min(heap)]

print(solution(operations=['I 16', 'D 1']))
print(solution(operations=['I 7', 'I 5', 'I -5', 'D -1']))