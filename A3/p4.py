def countWord():
    try:
        f = open("D:\D-48 Harsh Patel\A3\story.txt" , encoding="utf_8")
        lines = f.readlines()
        word = 0
        for line in lines:
            word += len(list(line.split()))
        print("TOTAL NO. OF WORDS : " , word)
    except OSError as e:
        print(e)

countWord()