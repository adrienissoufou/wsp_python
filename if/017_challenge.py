#Ask the use’s age, if they are 18 or over,
# display the message : " You can vote ",
# if they are aged 17, display the message
# " You can learn to drive "
#, if they are 16 , display the message 
# " You can buy a lottery ticket",
#if they are under 16, display the message 
# " You can go Trich-or-Treating".

print (" *** Wello ***")
age = int(input("entet your age : "))

if age >= 18:
    print("You can vote")
elif age == 17:
    print("You  can learn to drive.")
elif age == 16:
    print("You can buy a lottery tichet")
else:
    print("You can go Trich-or-Treating")
