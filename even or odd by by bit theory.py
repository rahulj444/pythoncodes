# finding whether the number is even or not
#by using lsg bit 
def function1(num):
    
    return (num&1)==0
num=int(input("enter the number:+=>"))
print(function1(num))

#by direclty 
def function1(num):
    
    return (num%2==0)
num=int(input("enter the number:+=>"))
print(function1(num))

#normal method by taking if else statements
def function1(num):
    
    if(num%2==0):
        return True
    else:
        return False
num=5
for num in range(10):
    print(num,function1(num),sep="\n")
'''0
True
1
False
2
True
3
False
4
True
5
False
6
True
7
False
8
True
9
False
'''