#palindrome number

def palindrome(num):
    
    if num==int(str(num)[::-1]):
        return True
    else:
        return False
num=int(input("enter a number:"))
print(palindrome(num))

# palindrome using another aproach by making then in anaother way
def palindrome(num):
    rem=0
    while num!=0:
        d=num%10
        rem=rem*10+d
        num=num//10
    return rem
num=int(input("enter a number:"))
print(num==palindrome(num))


