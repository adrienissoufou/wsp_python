#challenge 008
# Ask for the total price of the bill, 
# then ask how many diners there are.
# Divide the total bill by the number of diners
# and show how much each person must pay.

total  = int(input("what the total price of the bill ? : "))
nbrDiners = int(input("How many diners there are ? : "))

part = total / nbrDiners

print ("Everyone will pay", part )