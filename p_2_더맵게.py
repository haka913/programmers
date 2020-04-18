scoville = [2,1, 3, 9, 10, 12]
k = 7
import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    answer = 0
    isSpicy=True
    while True:
        if scoville[0]<k:
            if len(scoville)>1:
                a = heapq.heappop(scoville)
                b = heapq.heappop(scoville)
                heapq.heappush(scoville, a+b*2)
                answer+=1
            else:
                return -1
        else:
            return answer

print(solution(scoville, k))
