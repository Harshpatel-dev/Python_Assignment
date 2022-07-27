#readFile
from time import time

ans1 = []
ans2 = []

milliseconds1 = int(time() * 1000)

with open('words.txt' , 'r') as file:
    for line in file:
        for word in line.split():
           ans1.append(word)


milliseconds2 = int(time() * 1000)
  
print("Time in milliseconds using append method", milliseconds2)
print("Time in milliseconds using append method", milliseconds1)



milliseconds3 = int(time() * 1000)
  
with open('words.txt' , 'r') as file:
    for line in file:
        for word in line.split():
           ans2.append(word)


milliseconds4 = int(time() * 1000)
  
print("Time in milliseconds using + operator", milliseconds4 - milliseconds3)