
'''
LIST DATA STRUCTURE
---------------------------------------------------------------------
Introduction:
1. It is a group of objects.
2. It is represented by using [].
3. It allows heterogeneous objects (diffetent types of objects).
4. It allows indexing.
5. It supports both +ve and -ve indexing.
6. Slicing is allowed.
7. Insertion order is preserved.
8. Duplicates are allowed.
9. It is growable in nature. DURING execution(add/remove/update)
10. It is mutable i.e. modifications are allowed.


Creation of list objects:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. by using []
2. list()
3. split()
4. eval()
5. list comprehension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Example1:
L1 = [10, 20, 30, 40, 50]
s = "prakash"
L2 = list(s)
ss = "python is very easy"
L3 = ss.split()
---------------------------------------------------------------------
Accesing the list elements
~~~~~~~~~~~~~~~~~~~~~~~~~~
1.for loop
2.while loop
3.slice operator
4.index operator
5.directly we can print
------------------------------------
mathematical operations on list objects
---------------------------------------
+ list concatination

* repeat list object

l=[10,20,30]
print(3*l)#[10,20,30,10,20,30]

====================================

in and not in operators list
------------------------------
in---->true if given object it exits in list 
not in--->false if given object not exists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
comparing list objects:-
========================
we can compare two list objects based on contents ,the folloeing are the list of operators for comparing two list objects

<,>,>=,<=,==,!=

the return type of these operations always True or False

case1:-(<,<=,>=)
----------------
1.content of the first element
2.order of the elements
3.number of elements

print([10,20,30]<[10,20,40])#True
print([10,20,30]<=[10,20,40])#True
print([10,20,30]<[10,20,30])#False
print([10,20,30]<=[10,20,30])#True

case2:- == and !=
--------------------------
check the element each element if it equls 
-->return type is always T or F
print([10,20,30]==[10,20,30])#True
print([10,20,30]!=[10,20,40])#True
print([30,20,30]==[30,30,20])#False
               ********
list aliasing:
---------------
l1=[10,20,30,40]
l2=l1
print(l1)#[10,20,30,40]
print(l2)#[10,20,30,40] 

l1[1]=999
print(l1)--->#[999,20,30,40]
print(l2)---->#[999,20,30,40] 

print(l1==l2)---->#True
print(l1 is l2)--->#True     
----------------------------------
LIST CLONING
---------------------------------->
l1=[10,20,30,40]
l2=l1.copy          <-----*****
print(l1)#[10,20,30,40]
print(l2)#[10,20,30,40] 

l1[1]=999
print(l1)--->#[999,20,30,40]
print(l2)---->#[10,20,30,40] 

print(l1==l2)---->#False
print(l1 is l2)--->#False
--------------------------------->

Nested list:-same concept(13-(41.45))
-----------------------------
SHALLOW COPY AND DEEP COPY
---------------------------

import copy
l1=[1,23,4]
l2=l1

l1[1]=22
print(l1)
print(l2)
===>
[1, 22, 4]
[1, 22, 4]

DEEP COPY:-  
-------------
import copy
l1=[1,23,4]
l2=l1.copy()

l1[1]=22
print(l1)
print(l2)

[1, 22, 4]
[1, 23, 4]
------------------------------------

List comphrehension:-conditions inside the list

1.printing elements using list.
2.print squred elements using list.
3.cube of listed elements in list.


list methods:
============================
1.append
2.pop
3.clear
4.remove(ELEMENT)
5.extend
6.insert(index,object)
7.count(object)
8.list.reverse()
9.sort()
10.sort(reverse=True)
7.extend--->it adds the given iterable object to the list


L=[]
l1=[1,23,4]
l2={1,2,3}
l3="abc"

L.extend(l1)
L.extend(l2)
L.extend(l3)
print(L)

------------------------------------
OUTPUT:
------------------------------------

[1, 23, 4, 1, 2, 3, 'a', 'b', 'c']



=====================================



  





'''
L=[]
l1=[1,23,4]
l2={1,2,3}
l3="abc"

L.extend(l1)
L.extend(l2)
L.extend(l3)
print(L)























