s = 'baabaa'

# using stack
def solution(s):
    s = list(s)
    # print(s)
    st = []
    idx = 0
    while idx != len(s):
        st.append(s[idx])
        idx += 1
        if len(st) > 1:
            if st[-1] == st[-2]:
                st.pop()
                st.pop()
    if len(st) == 0:
        return 1
    else:
        return 0


print(solution(s))


# def solution(s):
#     answer = []
#     for i in s:
#         if not(answer):
#             answer.append(i)
#         else:
#             if(answer[-1] == i):
#                 answer.pop()
#             else:
#                 answer.append(i)
#     return not(answer)