import string
S="rahul jay balijaplly"

l1=[ele[0].upper()+ele[1:].lower() for ele in S.split(" ")]

print(l1)
print("*"*50)
 

print(string.capwords(S))

# sum of elements in list
def modu(lst):
    
    s=0
    
    for ele in lst:
        s+=ele
    return s
lst=eval(input(''))
k=sum(lst)
print(k)
print(modu(lst))
# sum of  even elements in list
def modu(lst):
    
    s=0
    
    for ele in lst:
        if ele%2==0:
            
            s+=ele
    return s
lst=eval(input(''))
k=sum(lst)
print(k)
print(modu(lst))      


def fun(n1,n2):
    
    l1=[i for i in range(n1,n2+1) if i%2==0]
    l2=[i for i in range(n1,n2+1) if i%2!=0]
    
    return l1,l2

n1=int(input(" number:"))
n2=int(input("enter the number:"))

print(fun(n1,n2))

def fun(n1,n2):
    
    l1=sum([i for i in range(n1,n2+1) if i%2==0])
    l11=[i for i in range(n1,n2+1) if i%2==0]
    l12=[i for i in range(n1,n2+1) if i%2!=0]
    l2=sum([i for i in range(n1,n2+1) if i%2!=0])
    
    return l1,l12,l2,l11

n1=int(input(" enter fisrt number:"))
n2=int(input("enter  second the number:"))

for i in fun(n1,n2):
    print(i)
    
import random
def fun():
    L=[]
    for i in range(10):
        L.append(random.randint(200,300))
    return L
print(fun())

 #reversing a list in python

def fun():
    leftindex = 0
    rightindex = len(l) - 1  # Use len(l) - 1 to get the last index
    while leftindex < rightindex:
        # Swap elements at leftindex and rightindex
        l[leftindex], l[rightindex] = l[rightindex], l[leftindex]
        leftindex += 1  # Increment leftindex by 1
        rightindex -= 1  # Decrement rightindex by 1
    return l

# Get input from user
l = eval(input("Enter the input: "))
print(fun())


# method number two

k = eval(input("Enter the input: "))
k.reverse()
print(k)

#max element in list using for loop

def maxi():

    l=eval(input(" enter the list"))
    max=l[0]

    for i in range(len(l)):
        if(max<l[i]):
            max=l[i]
    return max
print(maxi())









