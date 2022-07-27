#SORTING

def is_sorted(index , n , l):
    if(index == n):
        return True

    if(l[index -1 ] > l[index]):
        return False

    return is_sorted(index+1 , n ,l)

l = list(map(int , input("ENTER LIST OF NUMBERS : \n").split()))
n = len(l)
if(is_sorted(1 , n , l)):
    print("IT'S SORTED")
else:
    print("SORRY , SORT IT AGAIN !!!")





