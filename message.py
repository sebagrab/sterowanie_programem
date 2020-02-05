Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> somthingNumer='1000'
>>> print somthingNumer
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(somthingNumer)?
>>> print (somthingNumer)
1000
>>> somthingNumer+1
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    somthingNumer+1
TypeError: can only concatenate str (not "int") to str
>>> mesage = "Procesing file %s"
>>> print (masage % ('file.txt'))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print (masage % ('file.txt'))
NameError: name 'masage' is not defined
>>> print (mesage % ('file.txt'))
Procesing file file.txt
>>> massage2 = 'File %s has size %d KB'
>>> print (massage2 %('file.txt',100))
File file.txt has size 100 KB
>>> message3 ='file %20s has size %10d KB'
>>> print (message3 %('file.txt',100))
file             file.txt has size        100 KB
>>> message4 ="processing file {0:s}"
>>> message5 = 'File {0:s} has size {1:d}'
>>> message5.format('file.txt',100)
'File file.txt has size 100'
>>> 
================================ RESTART: Shell ================================
>>> 8*3
24
>>> five=5
>>> three=3
>>> five*three
15
>>> type(five)
<class 'int'>
\
>>> five/three
1.6666666666666667
>>> type(five/three)
<class 'float'>
>>> import sys
>>> sys.maxsize
2147483647
>>> veryBigValue=99999999999999999999999999999999999999999999999999
>>> type (veryBigValue)
<class 'int'>
>>> ((veryBigValue+1)/2)
5e+49
>>> five//three
1
>>> five %three
2
>>> float ('inf')
inf
>>> float ('inf')>99999999999999999999999999
True
>>> -float('inf)
       
SyntaxError: EOL while scanning string literal
>>> -float('inf')
-inf
>>> 