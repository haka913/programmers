def solution(tickets):
    route = {}
    answer = []

    for i in tickets:
        route[i[0]] = route.get(i[0], []) + [i[1]]
    for i in route:
        route[i].sort(reverse=True)

    s = ["ICN"]
    while s:
        top = s[-1]
        if top not in route or len(route[top]) == 0:
            answer.append(s.pop())
        else:
            s.append(route[top][-1])
            route[top] = route[top][:-1]

    answer = answer[::-1]
    return answer




print(solution(tickets=[['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
# print(solution(tickets=[['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))
# print(solution(tickets=[['ICN', 'BOO'], ['ICN', 'COO'], ['COO', 'DOO'], ['DOO', 'COO'], ['BOO', 'DOO'], ['DOO', 'BOO'],
#                         ['BOO', 'ICN'], ['COO', 'BOO']]))
