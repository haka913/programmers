import itertools

n = '1924'
k = 2

def solution(number, k):
    idx = 0
    result = []
    while idx != len(number):
        while k != 0 and result and result[-1] < number[idx]:
            result.pop()
            k -= 1

        result.append(number[idx])
        idx += 1
    for i in range(k):
        result.pop()

    return ''.join(result)


print(solution(n, k))

# todo  최고의 집합
# def solution(number, k):
#     answer = ''
#     list1 = list(map(''.join,itertools.combinations(number, len(number)-k)))
#     print(list1)
#     print(max(list1))
#     return answer

# def solution(number, k):
#     stack = [number[0]]
#     for num in number[1:]:
#         while len(stack) > 0 and stack[-1] < num and k > 0:
#             k -= 1
#             stack.pop()
#         stack.append(num)
#     if k != 0:
#         stack = stack[:-k]
#     return ''.join(stack)