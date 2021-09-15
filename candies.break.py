# To print no of available candies using break statement

av = 5 #av = Available candies

x = int(input("How many Candies you want ? "))

i = 1
while i <= x:

    if i > av:
          print("\ncandies out of stock ")
          break

    print("Candy", i)
    i+=1

print("\nNo Of Candies provided ", i-1)
print("No of Candies not provided ", x-(i-1))


print("\nThank You For  Shopping with us ")
print("Have a Great Day!")

print("\nVisit Soon")
print("Bye")

    
