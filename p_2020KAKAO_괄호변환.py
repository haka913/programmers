def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not p:
        return p
    answer = ""
    u, v = "", ""
    count_u = 0
    count_v = 0
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    for i, v in enumerate(p):
        if v == '(':
            count_u += 1
        else:
            count_v += 1
        if count_u == count_v:
            u = p[:i + 1]
            v = p[i + 1:]
            break

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    st = []
    for i in u:
        if i == '(':
            st.append(i)
        elif i == ')':
            if not st:
                st.append('N')
                break
            st.pop()

    if not st:  # st.size ==0
        u += solution(v)
    else:
        # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
        #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        #   4-3. ')'를 다시 붙입니다.
        u_tmp = "("
        u_tmp += solution(v)
        u_tmp += ")"
        #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        u = u[1:len(u) - 1]
        rev_uu = ""
        for i in u:
            if i == '(':
                rev_uu += ')'
            else:
                rev_uu += '('
        #   4-5. 생성된 문자열을 반환합니다.
        u_tmp += rev_uu
        return u_tmp

    # print(u, v, sep="\n")
    answer = u
    return answer


print(solution(p="(()())()"))
# print(solution(p=")("))
# print(solution(p="()))((()"))
# print(solution(p=""))
