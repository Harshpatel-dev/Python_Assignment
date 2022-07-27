#ANAGRAMS

s1,s2 = input().split()

#disctonary
mp = {}

if(len(s1) != len(s2)):
    print("THEY ARE NOT ....")

count = len(s1)

for i in range(0 , len(s1)):
    mp[s1[i]] = mp.get(s1[i] , 0) + 1

for i in range(0 , len(s2)):
    mp[s2[i]] = mp.get(s2[i] , 0) - 1 
    if(mp[s2[i]] >= 0):
        count -= 1

if(not count):
    print("THEY ARE ......")
else:
    print("THEY ARE NOT ......")
