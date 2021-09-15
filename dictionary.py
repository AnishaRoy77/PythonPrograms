Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # DICTIONARY we have a key and a value.
>>> dict = {1:'Hey', 2:'Anisha Roy'}
>>> dict
{1: 'Hey', 2: 'Anisha Roy'}
>>> dict = {1: 'Hey', 2: '1234'}
>>> dict
{1: 'Hey', 2: '1234'}
>>> #if we want to fetch a particular value we use []
>>> dict[2]
'1234'
>>> dict[1]
'Hey'
>>> dict[0]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict[0]
KeyError: 0
>>> #we can also use built in function of python to fetch the value by index number.
>>> dict.get(1)
'Hey'
>>> dict.get(2)
'1234'
>>> data[3]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    data[3]
NameError: name 'data' is not defined
>>> data.get(3)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    data.get(3)
NameError: name 'data' is not defined
>>> dict[3]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    dict[3]
KeyError: 3
>>> dict.get(3)
>>> print(data.get(3))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(data.get(3))
NameError: name 'data' is not defined
>>> 
>>> print(dict.get(3))
None
>>> 