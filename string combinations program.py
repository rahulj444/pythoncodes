
# abc permutations program
def function(s,ans=""):
    
    if len(s)==0:
        print(ans)
        
        
    else:
        for i in range(len(s)):
            function(s[i+1:]+s[:i],ans+s[i])
        
s='abc'
function(s)


print('#'*50)
def fun(s,ans=""):
    if len(s)==0:
        print(ans)
    else:
        for i in range(len(s)):
        
            fun(s[i+1:]+s[:i],ans+s[i])
s='123'
fun(s)






























