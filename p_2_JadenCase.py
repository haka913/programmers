s = "3people unFollowed me"
s = s.lower()
print(s)
lst = s.split()
for i in range(len(lst)):
    lst[i] = lst[i].capitalize()
print(" ".join(lst))
