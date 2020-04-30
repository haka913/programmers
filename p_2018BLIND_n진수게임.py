def baseN(number, base):
    numeral = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    result = ''
    if number == 0:
        return '0'
    while number > 0:
        result += numeral[number % base]
        number = number // base
    return result[::-1]


def solution(n, t, m, p):
    tmp = ''
    answer = ''
    for i in range(t * m):
        tmp += baseN(i, n)
    for i in range(p - 1, t * m, m):
        answer += tmp[i]

    return answer


print(solution(n=2, t=4, m=2, p=1))
print(solution(n=16, t=16, m=2, p=1))
print(solution(n=16, t=16, m=2, p=2))
