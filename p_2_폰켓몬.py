nums = [3,1,2,3]
answer=0
s1 = set(nums)
half = len(nums)//2
if len(s1)>=half:
    answer = half
else:
    answer = len(s1)



# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))