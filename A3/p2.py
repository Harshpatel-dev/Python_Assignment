def displayLine():
    try:
        f = open("D:\D-48 Harsh Patel\A3\poem.txt" , "r")
        lines = f.readlines()

        for line in lines:
            print(line , end="")
    except OSError as e:
        print(e)

displayLine()