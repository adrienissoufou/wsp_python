# Challenge 026 
# Pig Latin takes the first consonant of a word,
# move it to the end of the word and adds on 
# an "ay".
# if  a word begins with a vowel you just add 
# "way" to the end.
# For exempel:
# pig  -> igpay,
# banana -> ananabay
# aadvark -> aadvarkway
# Create a program that will ask the user 
# to enter a word and change it into Pig Latin.
# Make sure the new word is displayed in lower case
word  = input("Please enter Word : ")
farstOne = (word[0]).lower()
#print("the thirst word is : ",farstOne)

if farstOne == "a" or farstOne == "e" or farstOne == "i" or farstOne == "y" or farstOne == "o":
    word = word + "way"
    
else:
    #wordTemp =str.removeprefix(word,farstOne)
    wordTemp =word[1:len(word)]
    word = wordTemp + farstOne + "ay"
print ("your pig latin is : ", word.lower())