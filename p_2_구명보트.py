people = [70, 50, 80, 50]
limit = 100


def solution(people, limit):
    people.sort()
    light = 0
    heavy = len(people) - 1
    cnt = 0
    while light < heavy:
        if people[light] + people[heavy] <= limit:
            cnt += 1
            light += 1
            heavy -= 1
        else:
            heavy -= 1
    return len(people) - cnt


print(solution(people, limit))

