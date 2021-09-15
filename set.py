Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #SET  collection of unique elements and we use curly brackets.
>>> s = {1,2,3,4,5}
>>> s
{1, 2, 3, 4, 5}
>>> # set never follows sequence we have added those elements inside the brackets.
>>> 3 let's see :
SyntaxError: invalid syntax
>>> #lets see:
>>> s = {5 ,8,11,34,2,0,25}
>>> s
{0, 2, 34, 5, 8, 25, 11}
>>> # we cannot be sure with the sequence in set the reason is set uses a concept of "#" and using "#'we improves the performance we want to fetch the elements as fast as possible . lets see an example :
>>> s = {1 , 2, 4 ,5 ,2, 7, 9,7}
>>> s
{1, 2, 4, 5, 7, 9}
>>> # also in sets repeated numbers are printed only once.
>>> # in set index value is not supporte because we dont haave proper sequence.
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
>>> s[3]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s[3]
TypeError: 'set' object is not subscriptable
>>> 