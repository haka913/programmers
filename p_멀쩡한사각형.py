# boj 2168 타일 위의 대각선
import math
def solution(w,h):
    return w*h -w-h+math.gcd(w,h)

print(solution(w=8, h=12))