L=[1,2,5,8,6,2,5,9,1,8,8]
index = 0
while index < len(L):
    nbr = L[index]
    if L.count(nbr) > 1:
        L.remove(nbr)
    else:
        index +=1

print(L)