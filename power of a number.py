#power of a number

def power(x,y):
    
    return x**y
x=int(input("enter the base:"))
y=int(input("enter the power:"))
print(power(5,-1))

''''enter the base:10
enter the power:10
0.2'''



#power of a number

def power(x,y):
    mul=1
    for i in range(y):
        mul=mul*x
    return mul
    
    
x=int(input("enter the base:"))
y=int(input("enter the power:"))
print(power(5,3))

'''enter the base:5
enter the power:3
125
'''

