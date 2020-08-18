import copy

def solution(stones, k):
    left, right = 1, 200000000
    while left <= right:
        mid = (left + right) // 2
        tmp_stones = copy.deepcopy(stones)
        for i in range(len(tmp_stones)):
            tmp_stones[i] -= mid

        cnt = 0
        check = False
        for i in range(len(tmp_stones)):
            if tmp_stones[i] <= 0:
                cnt += 1
            else:
                cnt = 0

            if cnt >= k:
                check = True
                break
        if check:
            right = mid - 1
        else:
            left = mid + 1

    answer = left
    return answer


if __name__ == '__main__':
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
