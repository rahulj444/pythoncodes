
# finding the divisers for number
def divisors_numbers(n):
    L=[]
    
    for i in range(1,n+1):
        if n%i==0:
            L.append(i)
    return L
print(divisors_numbers(10))



# fo rlooping the every item
def divisors_numbers(n):
    L=[]
    
    for i in range(1,n+1):
        if n%i==0:
            L.append(i)
    return L

for i in range(20):
    print(i,divisors_numbers(i),sep="\t\t\t")