import string
S="rahul jay balijaplly"

l1=[ele[0].upper()+ele[1:].lower() for ele in S.split(" ")]

print(l1)
print("*"*50)
 

print(string.capwords(S))

# sum of elements in list
def modu(lst):
    
    s=0
    
    for ele in lst:
        s+=ele
    return s
lst=eval(input(''))
k=sum(lst)
print(k)
print(modu(lst))
# sum of  even elements in list
def modu(lst):
    
    s=0
    
    for ele in lst:
        if ele%2==0:
            
            s+=ele
    return s
lst=eval(input(''))
k=sum(lst)
print(k)
print(modu(lst))      


def fun(n1,n2):
    
    l1=[i for i in range(n1,n2+1) if i%2==0]
    l2=[i for i in range(n1,n2+1) if i%2!=0]
    
    return l1,l2

n1=int(input(" number:"))
n2=int(input("enter the number:"))

print(fun(n1,n2))


