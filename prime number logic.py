 # prime number logic in python with two differnt ways


def prime_number(n):
    
    factors=0
    
    for i in range(1,n+1):
        if n%i==0:
            factors+=1
    return factors==2

n=int(input("enter the input:"))
print(prime_number(n))

# method number two for finding prime number

def prime_number_2nd_way(n):
 
    for i in range(2,n):
        if n%i==0:
            return "not a prime"
    return "prime number"

n=int(input("enter the input:"))
print(prime_number_2nd_way(n))



















