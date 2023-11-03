def conversion_distance(km,m,cm):
    return km*1000 + m +cm/100

def convers_temp(h,m,s):
    return h*3600 + m*60 +s

def vitesse(T, D):
    return str(T)+"m/"+str(D)+"s"

print(vitesse(conversion_distance(56,3,9),convers_temp(5,2,9)))
