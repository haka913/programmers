def solution(s):
    ans = len(s)
    for size in range(1, ans // 2 + 1):
        ret = 0
        before, count = s[:size], 1
        for i in range(size, len(s), size):
            word = s[i:i + size]
            if word == before:
                count += 1
            else:
                if count > 1:
                    ret += len(str(count))
                ret += size
                before, count = word, 1

        if count > 1:
            ret += len(str(count))
        ret += len(before)
        ans = min(ans, ret)

    return ans


print(solution(s="xababcdcdababcdcd"))

# def solution(s):
#     def compress(size):
#         ret = 0
#         before, count = s[:size], 1
#         for i in range(size, len(s), size):
#             word = s[i:i + size]
#             if word == before:
#                 count += 1
#             else:
#                 if count > 1:
#                     ret += len(str(count))
#                 ret += size
#                 before, count = word, 1
#
#         if count > 1:
#             ret += len(str(count))
#         ret += len(before)
#         return ret
#
#     ans = len(s)
#     for size in range(1, ans // 2 + 1):
#         ans = min(ans, compress(size))
#
#     return ans
