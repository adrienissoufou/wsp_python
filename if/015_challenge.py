# Challenge 015
# Ask the user to enter their favourite colour.
# If they enter "red", "RED" or "Red" display the message 
# "I like red too"
#, otherwise display the message "I don't like [colour], i prefer red"

print("-- Hello --")

colore = input("enter your favourite color: ")
if colore == "red" or colore =="Red" or colore=="RED":
    print("I like red too.")
else:
    print("I don't like ", colore,", i prefer red. " )