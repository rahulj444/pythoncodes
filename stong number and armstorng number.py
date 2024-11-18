# armstrong number program

# sum of cubes to that number

def armstrong_number(n):
    
    s=0
    
    while n!=0:
        
        d=n%10
        
        s=s+d**3
        
        n=n//10
        
    return s

for i in range(10000):
    if i==armstrong_number(i):
        
        print(i)


# armstrong number program

# it is  strong number sum of factorails  is equal to
#that number

import math
def armstrong_number(n):
    
    s=0
    
    while n!=0:
        
        d=n%10
        
        s=s+math.factorial(d)
        
        n=n//10
        
    return s

for i in range(0,10000):
    if i==armstrong_number(i):
        
        print(i)




