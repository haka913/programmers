def solution(board, moves):
    position_list = [0]*len(board)
    stack = []
    answer = 0


    for y in range(len(board)):
        for x in range(len(board[0])):
            if(board[x][y] !=0):
                position_list[y] = len(board)-x
                break

    for pos in moves:

        if(position_list[pos-1]==0):
            continue

        if(board[len(board)-position_list[pos-1]][pos-1]!=0):
            temp = board[len(board)-position_list[pos-1]][pos-1]
            if(stack and temp == stack[-1]):
                stack.pop()
                answer +=1

            else:
                stack.append(board[len(board)-position_list[pos-1]][pos-1])
            board[len(board)-position_list[pos-1]][pos-1] = 0
            position_list[pos-1] -=1





    return answer*2




print(solution(board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], moves=[1,5,3,5,1,2,1,4]))