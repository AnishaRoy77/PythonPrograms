# Asking User to input value of array.

from array import*

arr = array('i',[])
n = int(input("Enter the Length Of The Array  :  "))

for i in range(n):
    x = int(input("Enter the Next value :  "))
    arr.append(x)

print(arr)              
