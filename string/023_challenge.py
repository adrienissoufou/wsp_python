#             Challenge 023
# Ask the user to type in the first line 
# of a nursery rhyme and display the length 
# of the string.
# Ask for a starting number and an ending 
# number and then display just that 
# section of the text
# (remember Python starts counting from 0 and not 1)
# exeple 
# Ils ne vous laissent jamais tranquilles
var = input("please enter your nursery rhyme : ")
varLen = len(var)
print("len : ", varLen)
cpt1 = int(input("what the starting number ? "))
cpt2 = int(input("what the end number ? "))

print(var[cpt1:cpt2])