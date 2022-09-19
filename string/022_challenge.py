# challenge 022
# Ask the user to enter their first name 
# and surname in lower case.
# Change the case to title case 
# and join them together.
# Display the finished result.
print ("please juste a lower case")
firstName = (input("please enter your first name : ")).title()
surName   = (input("please enter your surname : ")).title()

name = (firstName + " " + surName).strip(" ")

print("name ", name)