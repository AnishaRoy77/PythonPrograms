#To print numbers from 1 to 100 which are not divisible by 3 and 5

for i in range(1,100):
    
    if (i%3!==0 & i%5!==0):
        continue
    
    print(i)

print("\nEnd") 

      
