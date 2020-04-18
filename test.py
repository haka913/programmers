# import sys

# import this

# import time
#
# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# t = time.time()
# print(fibonacci(40))
# print('Python Elapsed % .02f' % (time.time() - t))

# print(sys.version)
# print("hello python")
#
# a, b = map(int, input().split())
# print(a + b)

# from datetime import datetime
#
# print(datetime.today().strftime("%Y-%m-%d"))
# memo = {0:1, 1:1}
# def fib(n):
#     if n in memo:
#         return memo[n]
#     else:
#         result = fib(n-1) + fib(n-2)
#         memo[n] = result
#         return result
#
# fib(15)
# print(memo)
# print(2/3)

# import math
# a,b = map(int, input().split())
# print(math.gcd(a,b))
# print(a*b//math.gcd(a,b))

# base, num = map(str, input().split())
# # ret = int(num, int(base)) % (int(base) - 1)
# # ret = int(str(ret), (int(base) - 1))
# # print(ret)

# n=1000
# a = [False,False] + [True]*(n-1)
# primes=[]
#
# for i in range(2,n+1):
#   if a[i]:
#     primes.append(i)
#     for j in range(2*i, n+1, i):
#         a[j] = False
# print(primes)

# s = input()
# s = s.lower()
# print(s)
# p = s.count('p')
# y = s.count('y')
# print(p, y)

# s = input()
# list1 = s.split(' ')
# answer =[]
# for i in list1:
#     s=''
#     for j in range(len(i)):
#         s+=i[j].upper() if j%2==0 else i[j].lower()
#     answer.append(s)
#
# print(' '.join(answer))

# chat = []
# chat.append(['님이 들어왔습니다','python '])
# print(chat)

# s = "hellopython"
# print(s[:3]+ " " + s[4:])
#
# name = "JEROEN"
# updown = list(range(14)) + list(range(12,0,-1))
# print(updown)
# updown = {chr(65+k):v for k, v in enumerate(updown)}
# print(updown)
# name = [updown[x] for x in name]
# print(name)

# n,m = map(int, input().split())
# list1 = [[j for j in range(m)] for i in range(n)]
# list1 = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
# for i in list1:
#     print(i)
# list2 = [list(x) for x in zip(*list1)]
# print(list2)
# list2.reverse()
# for i in list2:
#     print(i)

# 위(0,-1) 아래(0,1) 좌(-1,0) 우(1,0)
# dx = (0, 0, -1, 1)
# dy = (-1, 1, 0, 0)
# x,y=2,1
# print(list1[y][x])
# for i in range(4):
#     X = x+dx[i]
#     Y = y+dy[i]
#     print(list1[Y][X])

#
# n = int(input())
# for i in range(n-1,n+2):
#     print(i)

# a = list(map(int, input()))
# print(a)

# board1 = [[0]*3 for _ in range(3)]
# print(board1)
# board1[1][0]=2
# print(board1)
#
# board2 = [[0] * 3]*3
# print(board2)
# board2[1][0]=2
# print(board2)

# s = 'abcdefg'
# list1 = list(s)
# print(list1[-3:])
# print(list1)
# [list1.pop() for _ in range(3)]
# print(list1)


# a = list(input().strip())
# print(a)

# dx = -1, 0, 1, -1, 0, 1, -1, 0, 1
# dy = -1, -1, -1, 0, 0, 0, 1, 1, 1
#
#
# def check_beam(board, x, y):
#     return board[x][y - 1][0] or board[x + 1][y - 1][0] or (board[x - 1][y][1] and board[x + 1][y][1])
#
#
# def check_col(board, x, y):
#     return y == 0 or board[x][y - 1][0] or board[x][y][1] or board[x - 1][y][1]
#
#
# def solution(n, build_frame):
#     board = [[[0, 0] for _ in range(n + 2)] for _ in range(n + 2)]
#     for x, y, a, b in build_frame:
#         if a:
#             if b:
#                 if check_beam(board, x, y):
#                     board[x][y][1] = 1
#             else:
#                 board[x][y][1] = 0
#                 for d in range(9):
#                     nx, ny = x + dx[d], y + dy[d]
#                     if nx >= 0 and ny >= 0:
#                         if board[nx][ny][0] == 1:
#                             if not check_col(board, nx, ny):
#                                 board[x][y][1] = 1
#                                 break
#                         if board[nx][ny][1] == 1:
#                             if not check_beam(board, nx, ny):
#                                 board[x][y][1] = 1
#                                 break
#         else:
#             if b:
#                 if check_col(board, x, y):
#                     board[x][y][0] = 1
#             else:
#                 board[x][y][0] = 0
#                 for d in range(9):
#                     nx, ny = x + dx[d], y + dy[d]
#                     if nx >= 0 and ny >= 0:
#                         if board[nx][ny][0] == 1:
#                             if not check_col(board, nx, ny):
#                                 board[x][y][0] = 1
#                                 break
#                         if board[nx][ny][1] == 1:
#                             if not check_beam(board, nx, ny):
#                                 board[x][y][0] = 1
#                                 break
#     answer = []
#     for x in range(n + 2):
#         for y in range(n + 2):
#             if board[x][y][0]:
#                 answer.append([x, y, 0])
#             if board[x][y][1]:
#                 answer.append([x, y, 1])
#     answer.sort()
#     return answer
#
#
# print(solution(n=5, build_frame=[[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1],
#                                  [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
#
# print()
# print(pow(2, 3))
# print('hello')
# print([i*i for i in range(1,10)])


def index_of(elem, a):
    a_e = enumerate(a)
    a_f = list(filter(lambda x: x[1] == elem, a_e))
    if a_f:
        return a_f[0][0]
    else:
        return -1

a=[1,2,3,4,2]
a-=2
print(a)