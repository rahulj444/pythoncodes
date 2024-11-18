'''
Tuple Data structure:-
====================
Introduction:
1. It is a group of objects.
2. It is represented by using ().
3. It allows heterogeneous objects (diffetent types of objects).
4. It allows indexing.
5. It supports both +ve and -ve indexing.
6. Slicing is allowed.
7. Insertion order is preserved.
8. Duplicates are allowed.
9. It is not growable in nature. DURING execution(add/remove/update)
10. It is immutable i.e. modifications are not allowed.

Example:
---------------------
T=()
--------------------
Creation of tuple objects:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. by using ()
2. tuple()
3. eval()

Accesing the tuple elements
~~~~~~~~~~~~~~~~~~~~~~~~~~
1.for loop
2.while loop
3.slice operator
4.index operator
5.directly we can print
------------------------------------
mathematical operations on tuple objects
---------------------------------------
+ tuple concatination

* repeat tuple object

l=(10,20,30)
print(3*l)#(10,20,30,10,20,30)

====================================

in and not in operators list
------------------------------
in---->true if given object it exits in list 
not in--->false if given object not exists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
comparing tuple objects:-
========================
we can compare two list objects based on contents ,the folloeing are the list of operators for comparing two list objects

<,>,>=,<=,==,!=

the return type of these operations always True or False

case1:-(<,<=,>=)
----------------
1.content of the first element
2.order of the elements
3.number of elements

case2:- == and !=
--------------------------
check the element each element if it equls 
-->return type is always T or F
print([10,20,30]==[10,20,30])#True
print([10,20,30]!=[10,20,40])#True
print([30,20,30]==[30,30,20])#False
               ********
Nested list:-
-------------
same concept we can understand

Tuple  concepts:
============================
1.len
2.max
3.min
4.sorted(t)
5.sorted(t,reverse=True)
6.sum(t)

Tuple specific methods:
============================
1.count(object)==>count of object 
2.index()==>it retuens the index of value



tuple packing and unpacking:
---------------------------------------------
constructing a tuple obj from diff types of objects is called as packing. 
destructing a tuple obj into multiple objects is called as unpacking.

Example1:-


'''
w = 111
x = 222
y = 333
z = 444

t = w,x,y,z #tuple packing
print (w, type(w))
print(x, type(x))
print(y, type(y))
print(z,type(z))
print(t, type(t))
 
