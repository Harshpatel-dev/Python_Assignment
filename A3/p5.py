def countWord():
    try:
        count = 0
        f = open("D:\D-48 Harsh Patel\A3\checkUpper.txt" , encoding="utf_8")
        lines = f.readlines()
        for line in lines:
            for ch in line:
                if(ch.isupper()):
                    count+=1
        print("TOTAL NO. OF UPPERCASE CHARACTERS: " , count)
    except OSError as e:
        print(e)

countWord()