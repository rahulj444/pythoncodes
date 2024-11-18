'''
def linear_search(L,key):
    
    for i in range(len(L)):
        if L[i]==key:
            return i
    return

L=[1,2,3,4,5,6,7,78,8,90]
key=int(input("enter the number you want search:"))

print(linear_search(L, key))
print("*"*20)
def linear_search(L,key):
    
    for i in range(len(L)-1,1,-1):
        if L[i]==key:
            return i
    return

L=[1,2,3,4,5,6,7,7,7]
key=int(input("enter the number you want search:"))
print(linear_search(L, key))

def binary_search(L,key):
    low=0
    high=len(L)-1
    while low<=high:
        mid=(low+high)//2
        if key==L[mid]:
            return mid
        elif key<L[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
L=[1,2,3,4,5,6,7,8,9,10]
key=3
print(binary_search(L, key))

#using recursive call by returning in the queue
#------------------------------------------------ 
print("*"*15)
def binary_search(L,key,low,high):
 
    while low<=high:
        mid=(low+high)//2
        if key==L[mid]:
            return mid
        elif key<L[mid]:
            return binary_search(L, key, low, mid-1)
        else:
            return binary_search(L, key,mid+1, high)
    return -1
L=[1,2,3,4,5,6,7,8,9,10]
key=10
print(binary_search(L, key,0,len(L)-1))

def binary_search(L,key,low,high):
 
    while low<=high:
        mid=(low+high)//2
        if key==L[mid]:
            return mid
        elif key<L[mid]:
            return binary_search(L, key, low, mid-1)
        else:
            return binary_search(L, key,mid+1, high)
    return -1
L=[1,2,3,4,5,6,7,8,9,10]
key=5
print(binary_search(L, key,0,len(L)//2-1))
'''
# program for second half in list in the arguments we have to change
#--------------------------------------------------------------------
def binary_search(L,key,low,high):
 
    while low<=high:
        mid=(low+high)//2
        if key==L[mid]:
            return mid
        elif key<L[mid]:
            return binary_search(L, key, low, mid-1)
        else:
            return binary_search(L, key,mid+1, high)
    return -1
L=[1,2,3,4,5,6,7,8,9,10]
key=7
print(binary_search(L, key, len(L)//2-1, len(L)))

#program to find the elements in the given range

def binary_search(L,key,low,high):
 
    while low<=high:
        mid=(low+high)//2
        if key==L[mid]:
            return mid
        elif key<L[mid]:
            return binary_search(L, key, low, mid-1)
        else:
            return binary_search(L, key,mid+1, high)
    return -1
L=[1,2,3,4,5,6,7,8,9,10]
key=eval(input("enter the key value:==>"))
start=int(input("enter start vakue:==>"))
end=int(input("enter the second valu==>"))
print(binary_search(L, key,start,end))








