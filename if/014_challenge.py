#challenge 014 
#Ask the user enter a number between 10 and 20 (inclusive).
# if they enter a number within this range,
# display the message "Thank you" ,
# otherwise display the message "Incorrect answer".

print("-- Hello --")
nbr = int(input("plaise enter a number between 10 and 20 (inclusive):"))

if nbr >= 10 and nbr <=20:
    print("Thank you !")
else:
    print("Incorrect answer")