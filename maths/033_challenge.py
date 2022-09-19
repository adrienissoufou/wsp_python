#    Math Challenge  033
# Ask the user to enter two numbers.
# Use whole number division to divide the 
# first number by the second and also work 
# out the remainder and display the 
# answer in a user-friendly was 
# (e.g. if they enter 7 and 2 display 
# "7 divide by 2 is 3 with 1 remaining" 

nbr1 = int (input("please enter  1 : "))
nbr2 = int (input("please enter  2 : "))

var1 = nbr1 // nbr2
var2 = nbr1 % nbr2

print(nbr1 , " divide by ", nbr2 , " is ", var1 , " with ", var2 , " remaining ")