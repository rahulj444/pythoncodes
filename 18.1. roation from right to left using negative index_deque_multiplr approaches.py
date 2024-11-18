l=[1,2,3,4,5,6,7]
print(l[-1:-2:-1]+l[:len(l)-1])

#output:--->[7, 1, 2, 3, 4, 5, 6]

# the usage of the slice operator is when we come backward direction 
# we have to mention the step value as -1
# if not mentiond like that it could definatly the step moves from left to right
#version is same like this 

l=[1,2,3,4,5,6,7]
l.insert(0, l.pop(len(l)-1))
print(l)


def fun(l):
    
    n=len(l) # taken length of the list 
    x=l[n-1]  #assignet the last value to a 
    for i in range(n-1,0,-1):
        l[i]=l[i-1]
    
    l[0]=x
    return l

l=[1,2,3,4,5,6]
print(fun(l))


#anothr approach by using enque deque method
def fun(l,d):
    for i in range(d):
        l.append(l.pop(0))
    return l                # it is solved by using the general approach
l=[1,2,3,4,4,5]

 
print(fun(l,d=4))
# by using the reverse recursve and brute force apporcah in 

print('*'*50)

def reverse(L,s,e):
    while s<e:
        l[s],l[e]=l[e],l[s]  # created a reverse function to perform operation
        s+=1
        e-=1
        
        
def right_rotate(l,d):
    n=len(l)             # created a function in the system 
    reverse(l,0,d-1)     # from the start to d-1 since the d is less  #[]
    reverse(l,d,len(l)-1)  #from d to length-1
    
    reverse(l,0,len(l)-1)  # from 0 to length-1 reverse we get original
    
    return l
l=[1,2,3,4,5,6,7,8,9]
d=int(input(" enter the number of rotatons:--"))
print(right_rotate(l,d=4))

print('*'*50)


from collections import deque

l=[1,2,3,4,5,6]

dq=deque(l)

dq.rotate(2)  # from left to right w.r.t.computer  screen
print(list(dq))
dq.rotate(-2)  # rotates from right to left w.r.t to computer screen
print(list(dq))
#=========================================================

















    







