from math import hypot


# hypotenuse

import math

l = list(map(int , input("ENTER 'X' AND 'Y' : \n").split()))

print("HYPOTENUSE OF" ,l[0],"AND" , l[1] , "is :",int(math.hypot(*l)))