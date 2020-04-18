from itertools import cycle

answer = [1,3,2,4,2]


def solution(answers):
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores =[0,0,0]

    for st1, st2, st3,answer in zip(cycle(stu1),cycle(stu2),cycle(stu3),answers):
        if st1 == answer :
            scores[0] +=1
        if st2 == answer:
            scores[1] +=1
        if st3 == answer:
            scores[2] +=1

    stu =[]
    for i, score in enumerate(scores):
        if score == max(scores):
            stu.append(i+1)
    return stu

print(solution(answer))

