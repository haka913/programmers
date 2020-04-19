from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights[::-1]
    que = deque([0] * bridge_length)
    second = 0
    current_weight = 0

    while que:
        second += 1
        truck = que.popleft()
        if truck:
            current_weight -= truck
        if truck_weights:
            if current_weight + truck_weights[-1] <= weight:
                current_weight += truck_weights[-1]
                que.append(truck_weights.pop())
            else:
                que.append(0)

    return second


print(solution(bridge_length=2, weight=10, truck_weights=[7, 4, 5, 6]))
