import itertools
nums = [1,2,7,6,4]
n = 3000
list1 = [False, False] + [True] * (n - 1)
answer = []
for i in range(2, n + 1):
    if list1[i]:
        answer.append(i)
        for j in range(2 * i, n + 1, i):
            list1[j] = False

lis = list(itertools.combinations(nums,3))
# set으로 하면 틀림, 다른 숫자로 더하여도 같은 결과가 나올수 있으므로
lis1 = list([sum(i) for i in lis])
print(lis)
print(lis1)
answer = 0
for i in lis1:
    if list1[i]:
        answer +=1

print(answer)