Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #for addition
>>> 3+8
11
>>> #for substraction
>>> 5-3
2
>>> 3-5
-2
>>> #for multiplication in python
>>> 2*3
6
>>> #for division in python
>>> 3/6
0.5
>>> 4/2
2.0
>>> #2.0(is floating number ) to get integer number as output after divison we use "//"
>>> 4//2
2
>>> #to get remainder we use %
>>> 2%4
2
>>> 10%
SyntaxError: invalid syntax
>>> 10%3
1
>>> #python also follows bodmas rule for example
>>> 8+(2*3)
14
>>> (8+2)*3 #first according to the bodmas rule it will solvebracket one
30
>>> #in python we use double asterisks sign for example 2 power 3 we will write it as 2**3
>>> 2**3
8
>>> 2**2
4
>>> 4**2
16
>>> #whenever we  use string in python we use it within single or double quotes ""string" or 'string'.
>>> "Anisha"
'Anisha'
>>> 'Anisha'
'Anisha'
>>> #and we can also use print function to print string for example
>>> print('Anisha')
Anisha
>>> print('Anisha's laptop')
      
SyntaxError: invalid syntax
>>> #invalid syntax bcoz we can't simply have single quote any where like python here reads the special meaning of single quote as this s of anisha's is coming before the single quote so to avoid it we have to tell python to just skip the special meaning of the single quote by using backslash \ or we can use double quotes instead of single quotes here . let's see few examples based on this.
>>> print('Anisha\'s laptop)
      
SyntaxError: EOL while scanning string literal
>>> print('Anisha\'s laptop')
Anisha's laptop
>>> #or we can also use :
>>> print("Anisha's Laptop")
Anisha's Laptop
>>> #or we can also use :
>>> print('Anisha "laptop"') #if we want to print laptop in double quotes
Anisha "laptop"
>>> #also we can use :
>>> print('Anisha\'s "laptop" ')
Anisha's "laptop" 
>>> #if we want to add to strings i.e concatinate two strings we can use:
>>> 'anisha' + 'anisha'
'anishaanisha'
>>> #if we want anisha to get printed 10 times we use :
>>> 10 * 'Anisha'
'AnishaAnishaAnishaAnishaAnishaAnishaAnishaAnishaAnishaAnisha'
>>> #in python \n means new line let's see an example:
>>> print('a:\docs\new')
a:\docs
ew
>>> #in the above output we can see we got ew printed in new line and also it's is printed as ew not new aspython reads \n as single command which meand new line.
>>> #if we want to print the raw string that means the string as it is we use r before the quotes as r tells  python don't try to convert the \n into the special character. for example :
>>> print(r'a:\docs\new')
a:\docs\new
>>> 