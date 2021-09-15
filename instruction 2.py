Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>>  #lets assign the value of 2 to variable x
>>> x=2
>>> #now lets check the value is assigned to variable or not
>>> x+3
5
>>> #so in the above output we cAN SEE THAt x +3 = 5 so this proves that the value is assigned to variable.
>>>  y=3 #assigning value of 3 to variable y
 
SyntaxError: unexpected indent
>>> y=3 #assigning value of 3 to variable y.
>>> x+y #now adding both the variables.
5
>>> #now let's check whether we can change the value of variable by assigning differnt values .
>>> x=9
>>> x+y
12
>>> #so in the above output we can see that when we added x+y it gave 12 not 5 this means the value of variable can be changed.
>>> #if we want to use the output of the previous operation we use underscorei.e _ . underscore represents the output of the previous operation.
>>> #for example :
>>> 12+y #12 is the output of the previous operation 9+3 =12 .let's see without using underscore do we get an error or not.
15
>>> #cool it worked. we can also use underscore :
>>> _+y
18
>>> #we got 18 (the output of previous operation i.e 15(12+y =15) & 15+y =18 i.e 15+3 or _+y.
>>> #let's try assigning value with strings:
>>> name = 'Anisha Roy'
>>> name
'Anisha Roy'
>>> 'Anisha Roy'
'Anisha Roy'
>>> name + 'is a good girl'
'Anisha Royis a good girl'
>>> name[0] #if we want to fetch the first character of name = 'Anisha Roy'
'A'
>>> name[1]
'n'
>>> name[2]
'i'
>>> name[6]
' '
>>> name[7]
'R'
>>> name[10]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    name[10]
IndexError: string index out of range
>>> name[-1] #starts from the end i.e count from the last
'y'
>>> name[-4]
' '
>>> name[-2]
'o'
>>> name[-9]
'n'
>>> #it will print in reverse order as -ve sign starts or count from the end of the string.
>>> name[0:2] #if we want to print the 1st and the 2nd character together now here two doesn't mean no of characters it means ending, here it means the first two characters i.e 0 and 1.
'An'
>>> name[1:4] #it will start with i of anisha and end with h of anisha (it will end at 3 as we can't include 4 its exclusive of 4)
'nis'
>>> # mistaken in the above statement it will start with i of anisha and end with s not h .
>>> name[1:] #if we don't specify the wnding it wil print all the characters from 1.
'nisha Roy'
>>> #if we want to change the letter of string as Vanisha from Anisha can we ?
>>> #let's try with an example:
>>> name[0:3] = 'Hi' #trying to change string characters..
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    name[0:3] = 'Hi' #trying to change string characters..
TypeError: 'str' object does not support item assignment
>>> #oops it showed error! lets try with another example:
>>> name[0] = 'R'
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    name[0] = 'R'
TypeError: 'str' object does not support item assignment
>>> #so once we assign the value of string in python we cannot change it even for one character i.e strings in python are immutable.
>>> #but that doesn't mean we cannot change while printing ofcourse we can by using concatination method let's see how:
>>> 'Hi ' + name[0:]
'Hi Anisha Roy'
>>> #if we want to know the length of the string we can use the inbuilt function of python i.e len(string)
>>> myname = 'Anisha Roy'
>>> len(myname)
10
>>> 