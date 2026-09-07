Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
kyes = ["alice",28,"engineering"]
keys
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    keys
NameError: name 'keys' is not defined
kyes
['alice', 28, 'engineering']
user_profile = dict.fromkeys(kyes)
user_profile
{'alice': None, 28: None, 'engineering': None}
values=
SyntaxError: invalid syntax
values =["name","age","role"]
user_profile=dict(zip(kyes,values))
user_profile
{'alice': 'name', 28: 'age', 'engineering': 'role'}
dict={'name':'omm','age':20}
print "dict('name'):"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print ("dict('name'):")
dict('name'):
del dict('name');
SyntaxError: cannot delete function call
del dict['name']
user_profile
{'alice': 'name', 28: 'age', 'engineering': 'role'}
dict
{'age': 20}
dict.clear();
dict
{}
x='12'
x
'12'
x=int(x)
x
12
x=263.08
x
263.08
x=int(x)
x
263
type(x)
<class 'int'>
x=3846.97
type(x)
<class 'float'>
x='1110'
int(x,2)
14
int('A',16)
10
int(12,8)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(12,8)
TypeError: int() can't convert non-string with explicit base
>>> int('12',8)
10
>>> x = input("enter a number")
enter a number34
>>> x
'34'
>>> x=int(x)
>>> x
34
>>> x=str(x)
>>> x
'34'
>>> res=x
>>> res=x
>>> x='36'
>>> res=x+x
>>> res
'3636'
>>> res= x*3
>>> res
'363636'
>>> res=x-1
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    res=x-1
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> res=x/3
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    res=x/3
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> my_list =[1,3,2,4]
>>> type(my_list)
<class 'list'>
>>> my_tuple=tuple(my_list)
>>> my_tuple
(1, 3, 2, 4)
>>> type(my_tuple)
<class 'tuple'>
>>> x=4
>>> repr(x)
'4'
age = int(input('enter your age:'))

