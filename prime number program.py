def divisors_numbers(n):
    L=[]
    
    for i in range(1,n+1):
        if n%i==0:
            L.append(i)
    return L
print(divisors_numbers(10))