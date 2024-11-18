#rotate by using slice operator
l=[1,2,3,4,5,6]
k=int(input("enter the element you want where to split:"))

# in general method how to rotate
print(l[k:]+l[0:k])   #spliting for x to end and adding to 0 to end 
l.append(l.pop(k-1))
print(l)

def fun(l):  # create a function l
    n=len(l) # taking len to create for the furthur 
    x=l[0] # taking the first element as the value to append to x
    for i in range(1,n): # looping since the len will start from the start
        #shifting the location to previous one 
        l[i-1]=l[i]
        
    l[n-1]=x  # assiging the values to the first index without using ani built in
    return l  # reaturning the elements

l=[1,2,3,3,4,3] # inputing the list for the refereee
print(fun(l))   #


#################################################################

#rotate by number positions














