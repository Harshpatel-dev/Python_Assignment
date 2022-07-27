def cls():
    for i in range (1,50):
        print()

        
x,y = tuple(map(int , input().split(',')))

sum = 0
for i in range (0 , min(x,y)):
    sum += max(x,y)

print("SUM : " , sum)
cls()
