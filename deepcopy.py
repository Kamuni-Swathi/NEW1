l1 = ["idly","dosa"]
l2 = l1 #shallow copy
#l2 = l1.copy() #deep copy
l1.append("water")
print(l1)
print(l2)