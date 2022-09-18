#Challenge 18
# Ask the user to enter a number.
# If  it is under 10, display the message "Too low",
# if their number is between 10 and 20, display "Correct",
# otherwise display "Too high"

print (" Hello ")

nbr = int(input("enter a number : "))

if nbr < 10:
    print("Too low")
elif nbr > 10 and nbr < 20:
    print("Correct")
else:
    print("Too high")