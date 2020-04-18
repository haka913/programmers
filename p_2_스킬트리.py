skill = 'CBD'
skill_trees = ['BACDE', 'CBADF', 'AECB', 'BDA']


def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        temp = ""
        isSkill = True

        for s in st:
            if skill.find(s) !=-1:
                temp +=s
        # print("temp is " + temp)
        for i in range(len(temp)):
            if skill[i] != temp[i]:
                isSkill=False
                break

        if isSkill:
            answer +=1
    return answer

print(solution(skill,skill_trees))