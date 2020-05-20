def solution(routes):
    routes.sort()
    cam = 30000
    answer = 0

    for route in reversed(routes):
        if cam > route[1]:
            answer += 1
            cam = route[0]

    return answer


print(solution(routes=[[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
