def dfs(numbers, target, result, idx):
    if idx >= len(numbers):
        if result == target:
            global answer
            answer += 1
        return

    dfs(numbers, target, result + numbers[idx], idx + 1)
    dfs(numbers, target, result - numbers[idx], idx + 1)


def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target, 0, 0)
    return answer


print(solution(numbers=[1, 1, 1, 1, 1], target=3))
