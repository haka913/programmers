# 2020 카카오 인턴십2 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations


def solution(expression):
    op_list = ['+', '-', '*']
    op = []
    operand = expression.replace('+', ' ').replace('-', ' ').replace('*', ' ').split()
    answer = []

    for i in expression:
        if i == '-' or i == '*' or i == '+':
            op.append(i)

    for order in permutations(op_list):
        o1, o2, o3 = order
        tmp_operand = operand.copy()
        tmp_op = op.copy()
        while o1 in tmp_op:
            idx = tmp_op.index(o1)
            tmp_op.remove(o1)
            n1 = tmp_operand[idx]
            del(tmp_operand[idx])
            n2 = tmp_operand[idx]
            del(tmp_operand[idx])
            tmp_result = eval(n1+o1+n2)
            tmp_operand.insert(idx, str(tmp_result))

        while o2 in tmp_op:
            idx = tmp_op.index(o2)
            tmp_op.remove(o2)
            n1 = tmp_operand[idx]
            del(tmp_operand[idx])
            n2 = tmp_operand[idx]
            del(tmp_operand[idx])
            tmp_result = eval(n1+o2+n2)
            tmp_operand.insert(idx, str(tmp_result))

        while o3 in tmp_op:
            idx = tmp_op.index(o3)
            tmp_op.remove(o3)
            n1 = tmp_operand[idx]
            del(tmp_operand[idx])
            n2 = tmp_operand[idx]
            del(tmp_operand[idx])
            tmp_result = eval(n1+o3+n2)
            tmp_operand.insert(idx, str(tmp_result))
        answer.append(abs(int(tmp_operand[0])))

    return max(answer)


if __name__ == "__main__":
    print(solution("100-200*300-500+20"))  # 60420
    print(solution("50*6-3*2"))            # 300
