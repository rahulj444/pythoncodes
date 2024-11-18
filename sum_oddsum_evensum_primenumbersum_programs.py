#sum of digits
def sum1(n):
   
    sum=0

    while n!=0:
        d=n%10
        sum=sum+d
        n=n//10
    return sum
n=int(input("enter the number:"))
print(sum1(n))

#sum of digits of even numbers
def sum12(n):
   
    sum2=0

    while n!=0:
        d=n%10
        if d%2==0:
            sum2=sum2+d
            
        n=n//10
    return sum2
n=int(input("enter the number:"))
print(sum12(n))

#sum of digits of odd numbers
def sum_odd(n):
   
    sum2=0

    while n!=0:
        d=n%10
        if d%2!=0:
            sum2=sum2+d
            
        n=n//10
    return sum2
n=int(input("enter the number:"))
print(sum_odd(n))

#sumof odd and sum of even (#product of both those)
#sum of digits of odd numbers
def sum_odd_eve_mul(n):
   
    s=0
    s1=0

    while n!=0:
        d=n%10
        if d%2!=0:
            s=s+d
        else:
            s1=s1+d
                        
        n=n//10
    return s*s1
n=int(input("enter the number:"))
print(sum_odd_eve_mul(n))


# the sum of prime number in the a number 
def sum_prime(n):
    s=0
    while n!=0: #n>0: is also acceptable in the code
        d=n%10
        if d in (2,3,5,7):
            s=s+d
        n=n//10
    return s
n=int(input("enter the number:"))
print(sum_prime(n))






