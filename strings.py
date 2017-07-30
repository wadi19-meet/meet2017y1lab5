Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=['she','sells','sea','shells','by','the','sea','shore']
>>> b="selfish shellfish"
>>> c=[1 ,2 ,3 ,5 ,8 ,13]
>>> b[3:4]
'f'
>>> c[4]
8
>>> c[:-2]
[1, 2, 3, 5]
>>> a[3]
'shells'
>>> a[2:4]
['sea', 'shells']
>>> a[3:-1]
['shells', 'by', 'the', 'sea']
>>> a[3][:-1]
'shell'
>>> a[ 3]
'shells'
>>> a[3 ]
'shells'
>>> a[ 3]
'shells'
>>> b[8,14]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    b[8,14]
TypeError: string indices must be integers
>>> b[8:14]
'shellf'
>>> c[1]+c[2]
5
>>> 'by'
'by'
>>> 'by' in a
True
>>> 'self' in b
True
>>> a[2]==a[6]
True
>>> [1,2,3] in c
False
>>> 'sh' in c
False
>>> a[3]==b[8:13]
False
>>> dog='dalmatian'
>>> len(dog)
9
>>> dogs=[dog,'poodle','boxer']
>>> len(dogs)
3
>>> x,y,z=(3,4,5)
>>> my_tuple=(3,4,5)
>>> print(x+y+z)
12
>>> print(
