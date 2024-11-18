
def function(num,key):
    
    while num!=0:
        
        rem=num%10
        if rem==key:
            return True
        else:
            return false
num=int(input("enter a number:"))
key=int(input("key valuew:"))
print(function(num, key))

# with the number coversion with string
def function2(num,key):
    
    return str(num) in str(key)
num=int(input("enter a number:"))
key=int(input("key valuew:"))

print(function2(num, key))









