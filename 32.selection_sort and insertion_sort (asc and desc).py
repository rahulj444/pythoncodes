#selection sort
def selection(l):    
    for i in range(len(l)):
        min_index = i
        # Start by assuming the current position is the minimum
        for j in range(i + 1, len(l)):
            
            if l[min_index] < l[j]:
                
                min_index = j  # Update min_index if a smaller element is found    
    # Swap the elements
        l[i], l[min_index] = l[min_index], l[i]
    return l

l = [8,556,4999,532,66,233,5, 3, 6, 2, 4, 1]

print(selection(l))
print("*"*50)
#output in decening_order:-[4999, 556, 532, 233, 66, 8, 6, 5, 4, 3, 2, 1]


#selection sort
def selection(l):    
    for i in range(len(l)):
        min_index = i
        # Start by assuming the current position is the minimum
        for j in range(i + 1, len(l)):
            
            if l[min_index] > l[j]:
                
                min_index = j  # Update min_index if a smaller element is found    
    # Swap the elements
        l[i], l[min_index] = l[min_index], l[i]
    return l

l = [8,556,4999,532,66,233,5, 3, 6, 2, 4, 1]

print(selection(l))

#[1, 2, 3, 4, 5, 6, 8, 66, 233, 532, 556, 4999]
print("*"*50)




print("INSERTION_SORT_ASCENDENING "*2)


def insertion_sort_ASC(l):
    
    for i in range(1,len(l)):
        
        x=l[i]
        
        j=i-1
        
        while j>=0 and x<l[j]:
            
            l[j+1]=l[j]
            
            j=j-1
        l[j+1]=x
    
l = [8,556,4999,532,66,233,5, 3, 6, 2, 4, 1]
print(l)
insertion_sort_ASC(l)
print(l)

#[8, 556, 4999, 532, 66, 233, 5, 3, 6, 2, 4, 1]
#[1, 2, 3, 4, 5, 6, 8, 66, 233, 532, 556, 4999]






def insertion_sort_DES(l):
    for i in range(1,len(l)):
        
        x=l[i]  # Creating the evey element to start
        
        j=i-1  #better to compare to the lower one
        
        while j>=0 and x>l[j]: #using while checking and looping
            
            l[j+1]=l[j]
            
            j=j-1   #decrement the value for checking every elements
        l[j+1]=x   #assigning when all increses
        
l = [8,556,4999,532,66,233,5, 3, 6, 2, 4, 1]
print(l)
insertion_sort_DES(l)
print(l)
#[8, 556, 4999, 532, 66, 233, 5, 3, 6, 2, 4, 1]
#[4999, 556, 532, 233, 66, 8, 6, 5, 4, 3, 2, 1]



















