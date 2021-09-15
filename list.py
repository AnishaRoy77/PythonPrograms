Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #List (stores collection of data)                                                                                                                                                           (list can be written as a list of comma-separated values (items) between square brackets)                                                                                                    (A list may contain duplicate values with their distinct positions and hence, multiple distinct or duplicate values can be passed as a sequence at the time of list creation.                                                                                                                                                                                                                    Note – Unlike Sets, list may contain mutable elements.
>>> nums = [12,24,28,32,42,46]
>>> nums
[12, 24, 28, 32, 42, 46]
>>> nums[0]
12
>>> nums[1]
24
>>> #so here also we can pickup a number using index value i.e nums[index value]
>>> #we can also print something between till end or anywhere in the list by using nums[index value to be printed : value to be printed till ] let's see anexample below:
>>> nums[1:4]
[24, 28, 32]
>>> #in list  we can also  use negative range to fetch any element/character in the list.
>>> nums[-1]
46
>>> nums[-4]
28
>>> nums[-6]
12
>>> # we can also print strings using list.
>>> names = ['Anisha','Aman','Rahul']
>>> names
['Anisha', 'Aman', 'Rahul']
>>> # in list we can have different type lets see an example:
>>> values =[10.5 , 'Anisha' , 5]
>>> #in list we can also have list inside list .lets see :
>>> mil = [nums , names]
>>> mil
[[12, 24, 28, 32, 42, 46], ['Anisha', 'Aman', 'Rahul']]
>>> mil = [nums , names , values]
>>> mil
[[12, 24, 28, 32, 42, 46], ['Anisha', 'Aman', 'Rahul'], [10.5, 'Anisha', 5]]
>>> #num.append(value to be added) int the list we can also use num.insert(index value, value to be inserted).  the difference between append and insert is that append wil always add at the end of the list where as insert will insert the value between or anywhere we want .
>>> num.append(48)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    num.append(48)
NameError: name 'num' is not defined
>>> nums.append(48)
>>> nums
[12, 24, 28, 32, 42, 46, 48]
>>> nums.insert(3,30)
>>> nums
[12, 24, 28, 30, 32, 42, 46, 48]
>>> len(nums)
8
>>> #now if we want to remove any element from the list we use list name.remove(particular number) or if we want to remove any element by index number we use list name.pop(index number)
>>> nums.remove(24)
>>> nums
[12, 28, 30, 32, 42, 46, 48]
>>> nums.pop(3)
32
>>> nums
[12, 28, 30, 42, 46, 48]
>>> nums.pop()
