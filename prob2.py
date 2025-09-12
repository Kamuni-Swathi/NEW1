t = tuple(input().split(","))
i = int(input())
#t= list(t)
#t.pop(i)
#t = tuple(t)
#print(t)
t1 = t[0:i]
t2 = t[i+1:]
t = t1+t2
print(t)