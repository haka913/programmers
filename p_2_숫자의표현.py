n = 15

# n이 주어졌을 때 홀수인 약수의 개수
def solution(n):
    list1 = [i for i in range(1, n+1,2) if n%i is 0]
    answer = len(list1)
    return answer


print(solution(n))
