#Ask for two numbers.
#if the first one is larger
#than the second,  display the seconde 
# number first and then the first number,
#otherwise show the first number first and then the second.

print("---- Wello -----")
nbr1 = int(input("please input number 1 ? : "))
nbr2 = int(input("please input numbrer 2 ? : "))

if nbr1 < nbr2:
    print(nbr1 , " ", nbr2)
else:
    print(nbr2 ," ", nbr1)
print("see you.")