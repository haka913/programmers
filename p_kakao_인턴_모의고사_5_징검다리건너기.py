import numpy as np


def solution(stones, k):
    answer = 0
    stones_change = [ i-k for i in stones]
    # stones = np.array(stones) - k
    # print(stones)
    # print(stones_change)
    # min_x = 200000000
    # min_idx = 0
    idx_list = []
    min_list = []
    for i in range(len(stones_change) - k + 1):
        # if (min_x > sum(stones[i:i + k])):
        #     min_x = sum(stones[i:i + k])
        #     min_idx = i
        if (stones_change[i]<1 and stones_change[i+1] <1 and stones_change[i+2]<1):
            idx_list.append(i)
            min_list.append(sum(stones_change[i:i+k]))


    print(idx_list)
    print(min_list)
    answer_idx = min_list.index(min(min_list))
    # print("index is",answer_idx)
    # answer = max(stones_change[idx_list[answer_idx]:idx_list[answer_idx]+k])+k
    answer = max(stones[idx_list[answer_idx]:idx_list[answer_idx]+k])
    # print("answer is ", answer)


        # temp = stones[i:i+k]
        # for i in temp:
    # print(min_x)
    # print(min_idx)
    # print(max(stones[min_idx:min_idx+k])+k)
    # answer = max(stones[min_idx:min_idx + k]) + k
    return answer


# print(solution(stones=[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], k=3))
print(solution(stones=[2, 1, 2, 4, 3, 2, 1], k=3))

#Todo: 풀기