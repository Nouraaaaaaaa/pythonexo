
while True:
    val=int(input("enter your money:"))
    response = input("choose your conversion (euro to mad) or (mad to euro)")
    if(val <0):
        break
    elif response == "euro to mad":
        print("ur conversion to mad is :", val * 10.86)
    else:
        print("ur conversion euro is ",val * 0.092)
