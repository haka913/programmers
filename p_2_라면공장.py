import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    heap = []
    idx = 0
    while stock < k:
        for i in range(idx, len(dates)):
            if stock < dates[i]:
                break
            heapq.heappush(heap, -supplies[i])
            idx = i+1
        stock += heapq.heappop(heap)*(-1)
        answer += 1
    return answer


print(solution(stock=4, dates=[4, 10, 15], supplies=[20, 5, 10], k=30))
