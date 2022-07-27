def countLine():
    try:
        count = 0
        f = open("D:\D-48 Harsh Patel\A3\story.txt" , encoding="utf_8")
        lines = f.readlines()

        for line in lines:
            if(line != "" and (line[0] != 't' and line[0] != 'T')):
                count += 1
        print("NO. OF LINES WHICH IS NOT STARTING WITH 'T' OR 't' : " , count , end="")
    except OSError as e:
        print(e)

countLine()