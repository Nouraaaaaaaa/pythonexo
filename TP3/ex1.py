def fct(x,y):
    if(x < y):
        some = 0
        for i in range (x,y+1):
            some+=i
        
        return some
    else:
        return (fct(y,x))

print(fct(8,5))

