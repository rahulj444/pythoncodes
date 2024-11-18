def fun(a,b):
    
    '''to find addition of two numbers'''
    
    print(a+b)

fun(2,3)
print(fun.__doc__)

'''
creation of string objects in python:
======================================================

1. single quotes-------> normal input
2. double quotes---------->normal input
3. triple single quotes---->normal input
4. triple double quotes---->noraml input

5. input() function-------->input from the user as string 
6. str() type casting function-->type casting from (int,bool,complex)->str
7. eval()------------------->takes input from the user in quotes if string
                                 other wise its consider as normal object

'''
'''
slice operator ==>[]
======================
it starts with [0:len(string):step(default=1)]

for negative index==>
```````````````````````
[first index in negative:last index with negative:-1(to incrrease)]


print('abc'+99)===>error
print('abc'+'gef')==>abcgef

string repitaion operator(*): repeats the content in the string
    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('abc'*3)===>abcabcabc

print(2*'abc')====>abcabc

print('4'*'abc')====>error


membership operator (in,not in)=====>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print(a in 'rahul')===>True

print(k not in 'rahul')====>true

comapring string objects===>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example:
------------------
abc, abc------> 0,both are same
abc, ABC------->+32, abc > ABC
ABC, abc------->-32,ABC < abc




if we have two strings
s1==s2 ---> if all char ascii values are same
s1<s2-----> True if s1 < s2
s1>s2----> True if s1 > s2

Common functions on string objects:
``````````````````````````````````````````````````````````````
1. len(s)-----> number of characters present in s
2. max(s)--------> max char present in s based on ASCII
3. min(s)----> min char present in s based on ASCII
4. sorted(s)----> list with all characters sorted in asc order
5. sorted(s, reverse=True) --> list with all char in desc order
6.ord(ch)-------------> find the charecter for alphabet
7.chr(int)----------->find the char for the given ASCII code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Example:
s = "prakash"
print(s) #prakash
print(len(s)) #7
print(max(s)) #s
print(min(s)) #a
print(sorted(s)) #['a', 'a', 'h', 'k', 'p', 'r', 's']
print(sorted(s, reverse=True)) #['s', 'r', 'p', 'k', 'h', 'a', 'a']

print(chr(98))#b
print(chr(65))#A

print(ord('A'))#65



String Object is Immutable:-
~~~~~~~~~~~~~~~~~~~~~~~~~~`~
string object is immutable ;modifications
are not allowed on the string obj suppose if we are doing any modifications, with those modifications a new object will be created.
Ex:=
=============
s='python'
print(s)#python
s.upper()
print(s)#python
=================
example2:
==========
s='python'
print(s)#python
print(s.upper())#PYTHON

Ex:3:=
=============
s='python'
print(s)#python
s.upper()
print(s)#python
 
example4:
==========
s='python'
print(s)#python
print(s.upper())#PYTHON

========================================
String specific Methods:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
upper() -------> converts the given string into upper case
lower() -----> converts the given string into lower case
swapcase() ----> converts the given string from L to U and U to L
title() -----> converts each word first char into upper
capitalize() --> converts sentence first char into upper case
isalnum()------>:True if the given str contains only alpha numeric charecter
isalpha----->True if the given str contains only alphabets
isdigit()---->True if the given str contains only digits
isspace()---->True if the given str contains only place
islower()---->True if the given str contains only lower letter
isupper()---->True if the given str contains only upper letter



ExampleS:
========================================================
S = "PYTHON is Very eAsY to UNDERstand"
print(s) #PYTHON is Very eAsY to UNDERstand
print(s.upper()) #PYTHON IS VERY EASY TO UNDERSTAND
print(s.lower()) #python is very easy to understand
print(s.swapcase()) #python IS VERY EaSy TO underSTAND
print(s.title()) #Python Is Very Easy To Understand
print(s.capitalize()) #Python is very easy to understand


count():it count for the given sub-string, returns number of occurrences.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Example:
s = "abaabaaabaaaabc"
print(s.count('a')) #10
print(s.count('b')) #4
print(s.count('c')) #1
print(s.count('d')) #0
print(s.count("ab")) #4

replace():it replaces old string with new string
Example:
    
s = "abaabaaabaaaabc"
print(s.replace("ab","k")) #kakaakaaakc
print(s.replace("a", "w")) #wbwwbwwwbwwwwbc

startswith(str): it returns True if given str starts with another str
endswith(str): it returns True if the given str ends with another str

s = "python is very easy"
print(s.startswith("java")) #False
print(s.startswith("python")) #True
print(s.endswith("easy")) #True
print(s.endswith("difficult")) #False

index(str): it returns the index value of the given string else error.

find(str):it returns the index value of the given string else -1.
split(-):it returns the index value of the given string else -1.

separator.join(L):==>It joins the list of elements with separator.







































'''
















 