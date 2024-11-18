

def bubble_sorting(l):
    
    n=len(l)
    
    for i in range(n-1):
        swap=False
        for j in range(n-i-1):
            if l[j]<l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                swap=True
        if swap==False:   #by using the flag
            return 
                
l=[1, 2, 3, 4, 6, 7, 75, 687, 968]
print(l)
bubble_sorting(l) 
print("-"*30)

def bubble_sorting(l):
     
     n=len(l)
     
     for i in range(n-1): 
         for j in range(n-i-1):
             if l[j]<l[j+1]:        #decending order
                 l[j],l[j+1]=l[j+1],l[j]
                
                 
l=[7,6,9999,4,3,2,1]
print(l)
bubble_sorting(l)
print(l)

print("-"*30)
'''in decending order'''

def bubble_sorting(l):
     
     n=len(l)
     
     for i in range(n-1): 
         for j in range(n-i-1):
             if l[j]>l[j+1]:        #ascending order
                 l[j],l[j+1]=l[j+1],l[j]
                
                 
l=[7,6,687,968,75,4,3,2,1]
print(l)
bubble_sorting(l)
print(l)
print("-"*30)