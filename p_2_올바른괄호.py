s="(()("
answer = True

def isVPS(s):
    list1 =[]
    for i in s:
        if i=='(':
            list1.append(i)
        else:
            if list1:
                list1.pop()
            else:
                return False

    return False if list1 else True

print(isVPS(s))

