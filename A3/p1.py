

# from pickle import TRUE


def findName():
    try:
        s = input("ENTER NAME TO BE FOUND : ")
        f = open("D:\D-48 Harsh Patel\A3\student.txt" , "r")
        lines = f.readlines()

        for line in lines:
            if(line.strip() == s):
                print("ANSER -->","GIVEN STRING EXIST.....")
                f.close()
                return
        print("ANSER -->","OPPS..  GIVEN STRING DOESN'T EXIST.....")
        f.close()
    except OSError as e:
        print(e)


def addName():
    s = input("ENTER NAME TO BE ADDED : ")
    f = open("D:\D-48 Harsh Patel\A3\student.txt","a")
    s += "\n"
    f.write(s)
    print("ANSER -->","ADDED..")
    f.close()

menu = '''
    1. Enter a name to add
    2. Enter a name to find
    3. exit
'''

while True :
    print(menu)
    takenInput = int(input("Enter your Choice : "))

    if(takenInput == 1):
        addName()
    elif(takenInput == 2):
        findName();
    else:
        exit(0)