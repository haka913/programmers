def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        str1 = bin(arr1[i] | arr2[i])[2:]
        # str1 = str1[2:]
        #str1 = '0'*(n-len(str1))+str1
        str1 = str1.rjust(n,'0')
        # print(str1)
        temp = str1.replace('1','#').replace('0',' ')
        answer.append(temp)
    return answer


# 오른쪽 정렬은 rjust 라는 함수를 사용하고, 왼쪽 정렬은 ljust 라는 함수를 사용하면 됩니다.
#
# a = "123"
# print a.rjust(10, '#')
# 결과 = '#######123'
# 출처: https://ngee.tistory.com/397 [ngee]

# print(solution(n=5, arr1=[9, 20, 28, 18, 11], arr2=[30, 1, 21, 17, 28]))
print(solution(n=6, arr1=[46, 33, 33, 22, 31, 50], arr2=[27, 56, 19, 14, 14, 10]))
