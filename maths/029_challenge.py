# Math Challenge 029 
# Ask the user to enter an integer that in over 500.
# Work out the square root of that number 
# and display it to two decimal places.
import math

num1 = int(input("enter an integer that in over 500 : "))

num2 = round(float(math.sqrt(num1)),2)

print(" num2 : ", num2)