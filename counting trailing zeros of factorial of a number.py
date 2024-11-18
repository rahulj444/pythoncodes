import math
x=int(input("enter a number:"))
f=math.factorial(x)

count=0
while f!=0:
    if f%10!=0:
        break
    else:
        f=f//10
        count+=1
print(count)


f=math.factorial(20)
print(f)

'''enter a number:20
4
2432902008176640000'''