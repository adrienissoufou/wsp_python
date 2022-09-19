# Math Challenge 032
# Ask for the radius and depth of a cylinder
# and work out the total volume
# ( circle area * depth)
# rounded to three decimal place.
import math
var = float(input(" please enter raduis of a cicle : "))
my_depth = float(input(" please enter depth of a cylinder : "))

areaCicle = math.pi * var**2

cylinder = round(areaCicle * my_depth,3)

print("total volume : ", cylinder)