l =[1,3,5,6,1,0,1]
val = int(input("enter nbr :"))
list_acc = []
count = 0
index = 0
while index < len(l):
    if l[index] == val:
        count +=1
        list_acc.append(index)
    index +=1
print ("le nbr docc de ",val ,"est:",count,"les positions sont:",list_acc)
