L= [5,1,3] 
size = int(len(L)-1)
print(size)
i=0
while i <= (size/2)+1:
    swap = L[i]
    L[i] = L[size]
    L[size]=swap
    i+=1
    size-=1
print(L)