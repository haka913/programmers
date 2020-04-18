n = 8
a = 4
b = 7

def solution(n, a, b):
    cnt = 0

    while a!=b:
        a = a//2+ a%2;
        b = b//2+b%2;
        cnt+=1
    return cnt

print(solution(n,a,b))


# def solution(n,a,b):
#     return ((a-1)^(b-1)).bit_length()