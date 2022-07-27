#x = list(map(str , input().split()))

x = input("Enter a number : ")

s = ("").join(x.split("-"))

if(len(s) == 10 and s.isdigit()):
    print("Valid")
else:
    print("Invalid")
