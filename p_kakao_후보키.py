from itertools import combinations
def solution(relation):
    people = len(relation)
    cols = len(relation[0])
    colList = range(cols)
    def isCandidate(colList, people):
        tmp = [tuple([item[i] for i in colList]) for item in relation]
        print(tmp)
        if len(set(tmp)) != people:
            return False
        else:
            return True

    result = []
    for i in range(1,cols+1):
        comb = combinations(colList, i)
        # print('comb', list(comb))
        for j in list(comb):
            if isCandidate(j, people):
                result.append(set(j))

    print(result)
    for el1 in result[:]:
        for el2 in result[:]:
            print(el1, el2)
            # print("set intersection")
            # print(el1&el2)
            # print()
            # if el1 == el1 & el2:
            #     if el1 != el2:
            #         result.remove(el2)
    # print(result)
    answer = 0
    return answer


print(solution(
    relation=[["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
              ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))

