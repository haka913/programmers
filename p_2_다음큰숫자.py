n = 78
def solution(n):
    bi_len = bin(n).count('1')
    for i in range(n+1, 1000001):
        if bin(i).count('1') == bi_len:
            return i

print(solution(n))