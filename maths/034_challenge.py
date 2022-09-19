#Display the following massage :
#      1) Square
#      2) Triangle

# If the user enters 1, then it should ask them for
# the length of one of its sides and display the area.
# If they select 2, it should ask for the base and
# height of the triangle and
# display the area.
# if they type in anything else, 
# it should give them a suitable error message.

print("""
        1) Square.
        2) Triangle
      """)

choix = input("enter your choise 1 / 2 : ")
if choix == "1":
    square = int(input("length of one of its sides : "))
    ereaOFsquare =  square * square
    print(" the area of Square : ", ereaOFsquare)
elif choix == "2":
    myBase = int(input("base of trianle : "))
    myHeight = int(input("height triangle : "))
    ereaOFtriangle = 1/2 * myBase * myHeight
    print(" the area of triangle : ", ereaOFtriangle)
else:
    print("choise note exite, ERROR MESSAGE")


