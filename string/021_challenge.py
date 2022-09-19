# challenge 021
# Ask the user to enter their first name and
# then ask them to enter their surname.
# Join them together with a space between
# and display the name and the length of whole name.

firstName = input("please enter your first name : ")
surName   = input("please enter your surname : ")

name = (firstName + " " + surName).strip(" ")

print("name ", name , "length ", len(name))