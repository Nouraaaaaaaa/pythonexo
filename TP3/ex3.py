def convers_temp(h,m,s):
    return h*3600 + m*60 +s

def conversion_distance(km,m,cm):
    return km*1000 + m +cm/100


print(convers_temp(5,20,40))