# Ask the user to enter their first name.
# if the length of their first name 
# is under five characters,
# ask them to enter their surname and join them
# together (without a space) and display the 
# name in upper case.
# If the length of the first name is 
# five or more characters,
# display their fist name in lower case

from os import PRIO_USER
from unicodedata import name


firstName = input("please enter your first name : ")
firstNameLen = len(firstName)
if firstNameLen < 5:
    surName   = input("please enter your surname : ")
    name = firstName + " " + surName
    print("your name in upper case : ", name.upper())
else:
    print("your first name in lower case", firstName.lower())