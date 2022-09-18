# Challenge 013 
# Ask the user to enter a number that is under 20.
# If they enter a number that is 20 or more ,
# display the message "Too high",
# otherwise display "thank you".

print("-- Hello --")
nbr = int(input("plaise enter a number that is under 20 :"))

if nbr < 20:
    print("Thank you !")
else:
    print("Too high")