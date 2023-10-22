l=[0,1,5,12]
val = 14
index = 0
while index < len(l) and l[index] < val:
    index += 1



l.insert(index, val)
print(l)