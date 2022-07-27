def cls():
    for i in range (1,50):
        print()

def feet_inches(feet):
    #global inches
    inches = feet*12
    return inches

def inches_feet(inches):
    #global feet
    feet = inches/12
    return feet

feet = int(input("ENTER FEET TO CONVERT INTO INCHES : "))
inches = int(input("ENTER INCHES TO CONVERT INTO FEET : "))

print("AFTER CONVERTING FEET TO INCHES : " , feet_inches(feet))
print("AFTER CONVERTING INCHES TO FEET : " , inches_feet(inches))

cls()
