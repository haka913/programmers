citations = [3, 0, 6, 1, 5]


# citations = [10,50,100]

# 여기서 i+1은 인용된 논문의 수인데
# 이렇게 인용 횟수가 인용된 논문의 수보다 작아지는 순간이 H-Index보다 1 커지는 순간이며
# 고로 그 전의 index를 return하면 답을 도출해낼 수 있다.
# 마지막까지 조건문에 안걸리는 경우도 있는데 이 경우
# 답이 나올 경우의 수는 H-index가 논문의 수 그 자체인 경우밖에 없으므로
# 이것을 return한다.

def solution(citations):
    citations.sort(reverse=True)
    for i, x in enumerate(citations):
        if x < i + 1:
            return i
    return len(citations)


print(solution(citations))
