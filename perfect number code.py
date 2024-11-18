# perfect number code in python 

#the logic code is sum of the divisors == given number thats it in the python

def perfect_number(n):
    s=0
    
    for i in range(1,n):
        if n%i==0:
            s=s+i
    return s==n 
n=int(input("enter a number:"))
for i in range(n):
    if perfect_number(i):
        print(i)
        
            