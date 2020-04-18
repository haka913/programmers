def solution(name):
    init = ['A'] * len(name)
    name = list(name)
    cnt = 0
    idx = 0
    while init != name:
        rightidx = 1
        leftidx = 1
        if name[idx] != 'A':
            if ord(name[idx]) - ord('A') > 13:
                cnt += 26 - (ord(name[idx]) - ord('A'))
            else:
                cnt += ord(name[idx]) - ord('A')
            name[idx] = "A"

        if name == init:
            break
        else:
            for i in range(1, len(name)):
                if name[idx + i] == 'A':
                    rightidx += 1
                else:
                    break
                if name[idx - i] == 'A':
                    leftidx += 1
                else:
                    break

            if rightidx > leftidx:
                cnt += leftidx
                idx -= leftidx
            else:
                cnt += rightidx
                idx += rightidx
    return cnt


# print(solution(name="JAN"))

# boj 3663

# def solution1(name):
#     updown = list(range(14)) + list(range(12,0,-1))
#     updown = {chr(65+k):v for k, v in enumerate(updown)}
#     name = [updown[x] for x in name]
#     right = 0
#     left = 0
#     for i in range(len(name)-1):
#         if name[1+i] != 0:
#             break
#
#         right += 1
#     for i in range(len(name)-1):
#         if name[-i-1] != 0:
#             break
#
#         left -= 1
#     return sum(name) + len(name) - 1 - max(left, right)
