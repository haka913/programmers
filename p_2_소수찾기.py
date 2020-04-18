import itertools

numbers = "17"
def solution(numbers):
    answer = set()
    time = 10 ** len(numbers)
    print(time)
    list1 = [False, False] + [True] * (time - 1)
    for i in range(2, time):
        if list1[i]:
            for j in range(2 * i, time, i):
                list1[j] = False

    nums = list(numbers)
    for i in range(1, len(numbers) + 1):
        lis = list(map(''.join, itertools.permutations(nums, i)))
        for i in lis:
            num = int(i)
            if list1[num]:
                answer.add(num)
    return len(answer)

print(solution(numbers))
# Todo:  2018 kakao blind recruitment 무지의 먹방라이브