def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d


a = int(input("Enter First Number :  "))
b = int(input("Enter Second Number : "))
result1 , result2 = add_sub(a,b)
print("The sum of two numbers are : " ,result1)
print("The subtraction  of two numbers are : " ,result2)

