Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:/Users/seba/Documents/Python Scripts/print.py ===========
Francja
fr usa belgia
>>> 
=========== RESTART: C:/Users/seba/Documents/Python Scripts/print.py ===========
Francja
fr usa belgia
fr belgia
>>> 
=========== RESTART: C:/Users/seba/Documents/Python Scripts/print.py ===========
Francja
fr usa belgia
fr belgia
3.14 10
Traceback (most recent call last):
  File "C:/Users/seba/Documents/Python Scripts/print.py", line 8, in <module>
    pint (pi,r,pi*r*r)
NameError: name 'pint' is not defined
>>> 
=========== RESTART: C:/Users/seba/Documents/Python Scripts/print.py ===========
Francja
fr usa belgia
fr belgia
3.14 10
3.14 10 314.0
>>> 
=========== RESTART: C:/Users/seba/Documents/Python Scripts/print.py ===========
Francja
fr usa belgia
fr belgia
3.14 10
3.14 10 314.0
1 2 3
1-2-3
fr
usa
be
this is a bell 
tis is backslash \
>>> atext='this is a text'
>>> atext.endswith('ext')
True
>>> atext.islower()
True
>>> atext.upper()
'THIS IS A TEXT'
>>> atext.upper().isupper()
True
>>> atext.find('is')
2
>>> atext.find('is',3)
5
>>> atext.replace('a','4')
'this is 4 text'
>>> atext.replace('a','4').replace('i','1')
'th1s 1s 4 text'
>>> atext.spilt(' ')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    atext.spilt(' ')
AttributeError: 'str' object has no attribute 'spilt'
>>> atext.split(' ')
['this', 'is', 'a', 'text']
>>> somthingLikeNumber='1000'
>>> somehingLikeNumber+1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    somehingLikeNumber+1
NameError: name 'somehingLikeNumber' is not defined
>>> somehingLikeNumber.isdigital()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    somehingLikeNumber.isdigital()
NameError: name 'somehingLikeNumber' is not defined
>>> somthingLikeNumber.isdigital()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    somthingLikeNumber.isdigital()
AttributeError: 'str' object has no attribute 'isdigital'
>>> 
================================ RESTART: Shell ================================
>>> drive = 'c:\\'
>>> folder = 'scripts\\python\\'
>>> file = 'myscript.py'
>>> path = drive+folder+file
>>> print (path)
c:\scripts\python\myscript.py
>>> path
'c:\\scripts\\python\\myscript.py'
>>> justText = 'text with\nnew line'
>>> print(jurtText)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(jurtText)
NameError: name 'jurtText' is not defined
>>> print(justText)
text with
new line
>>> justText = r'text with\nnew line'
>>> print(justText)
text with\nnew line
>>> justText = "mc donald's"
>>> print(justText)
mc donald's
>>> justText = 'mc donald's'
SyntaxError: invalid syntax
>>> justText = 'mc donald\'s'
>>> print(justText)
mc donald's
>>> firstName = 'Kasia'
>>> famillyName = 'Sowa'
>>> lastName = 'Mrugała'
>>> newName=(firstName+" " +famillyName+" " +lastName)
>>> print(newName)
Kasia Sowa Mrugała
>>> music = "\"Universal Fanfare\" Jerry Goldsmith \"Happy Together\" Garry Bonner \"I\'m a Man\" Steve Winwood "
>>> print(music)
"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I'm a Man" Steve Winwood 
>>> music = "\"Universal Fanfare\" Jerry Goldsmith\n \"Happy Together\" Garry Bonner\n \"I\'m a Man\" Steve Winwood "
>>> print(music)
"Universal Fanfare" Jerry Goldsmith
 "Happy Together" Garry Bonner
 "I'm a Man" Steve Winwood 
>>> print("(\(\ ")
(\(\ 
>>> print("(\(\ "\n,"( -.-)\n","O_(\")(\")"
      
SyntaxError: unexpected character after line continuation character
>>> print("(\(\ "\n,"( -.-)\n","O_(\")(\")")
SyntaxError: unexpected character after line continuation character
>>> print("(\(\ \n","( -.-)\n","O_(\")(\")")
(\(\ 
 ( -.-)
 O_(")(")
>>> print(" (\(\ \n","( -.-)\n","O_(\")(\")")
 (\(\ 
 ( -.-)
 O_(")(")
>>> numer = '1000'
>>> print(numer)
1000
>>> numer +1
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    numer +1
TypeError: can only concatenate str (not "int") to str
>>> int(numer)+1
1001
>>> numer+str(1)
'10001'
>>> 