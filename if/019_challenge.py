#Challenge 019
#Ask the user to enter 1, 2 or 3 .
#If they enter a 1, display the message "Thank you", 
#if they enter a 2, display "Well done", 
#if they enter a 3, display "Correct".
#If they anything else, display "Error message"

print("%%%  Hello %%%")
nbr = int(input("please,  enter 1, 2 or 3 : "))
if nbr == 1:
    print("Thank you")
elif nbr == 2:
    print("Well done")
elif nbr == 3:
    print("Correct")
else:
    print("Error message")