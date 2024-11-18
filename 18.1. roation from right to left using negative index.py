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
