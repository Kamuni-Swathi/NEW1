t = tuple(map(int,input().split(",")))
m = t[0]
for i in t:
    if t.count(i)>t.count(m):
        m = i
print(t.count(m))        