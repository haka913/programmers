from fractions import gcd
def solution(arr):
    lcmResult = 1
    for i in arr:
        currentGCD = gcd(lcmResult,i)
        lcmResult = lcmResult*i/currentGCD
    answer = lcmResult
    return answer