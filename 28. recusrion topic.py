'''#functions

def fun(n):
    if n==0:
        return 0
    return n%10 +fun(n//10)
print(fun(123345))

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

for i in range(10):
    print(fib(i),end=" ")
    
def f(n):
    if n==0 or n==1:
        return 1
    return n*f(n-1)

for i in range(10):
    print(f(i),end="")

def pow(a,b):
    if b==0:
        return 1
    return a*pow(a,b-1)
print(pow(11,3))
    
    '''
 
    

    
    