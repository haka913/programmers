import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

numbers = [5,546]

lis = list(map(str, numbers))
lis.sort(key=functools.cmp_to_key(lambda x,y:int(x+y)-int(y+x)),reverse=True)

print((1>2)-(1<2))