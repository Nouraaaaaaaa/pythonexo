import random
rand_nbr =random.randint(1,100)
for i in range(0,7):
    nbr = int(input("enter an nbr:"))
    if nbr < 0 or nbr > 100:
        print("you are out of interval")
        continue
    elif nbr < rand_nbr:
        print("bigger")
    elif nbr == rand_nbr:
        print("great",nbr,"is the right nbr you get it in",i+1,"test")
        break


if i == 6:
    print("ops! good luck for the next time")
