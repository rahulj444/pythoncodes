def number_repitations(n):
    
    l=[]
    count=0
    while n!=0:
        
        d=n%10
        count=count+1
        n=n//10
    return count
n=int(input(" enter a number:"))
print(number_repitations(n))


