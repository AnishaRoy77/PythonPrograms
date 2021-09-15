Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums = [12,46,48]
>>> nums
[12, 46, 48]
>>> del nums[2:]
>>> nums
[12, 46]
>>> nums.extend([49,50,51,52])
>>> nums
[12, 46, 49, 50, 51, 52]
>>> max
<built-in function max>
>>> max(nums)
52
>>> min(nums)
12
>>> sum(nums)
260
>>> sub(nums)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sub(nums)
NameError: name 'sub' is not defined
>>> nums.sort()
>>> nums
[12, 46, 49, 50, 51, 52]
>>> 