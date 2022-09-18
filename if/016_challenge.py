#Challenge 016
# Ask the user if it is raining and convert 
# their answer to lower case
# so it doesn’t matter what case they type it in.
#
# if they answer « yes », ask if it is windy. 
# if they answer « yes » to this seconde question,
# display the answer « it is too windy for an umbrella »,
# otherwise display the message « take an umbrella » .
# if they did not answer yes to the first question, 
# display the answer « Enjoy your day ».

print(" === Wellop === ")
answer1 = input("it is raining=, : ")

answer1 = str.lower(answer1)


if answer1 == "yes":
    how = input("it is windy? : ")
    how = str.lower(how)
    if how =="yes":
        print(" it is too windy for an umbrella")
    else:
       print("take an umbrella")
else:
    print("Enjoy your day ")