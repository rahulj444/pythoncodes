'''def towers(n, src, temp, dest):
    if n == 1:
        print(f"move disk {n} from {src} to {dest}")
        return
    towers(n - 1, src, dest, temp)
    print(f"move disk {n} from {src} to {dest}")
    towers(n - 1, temp, src, dest)

n = int(input("Enter number of disks: "))
towers(n, "S", "T", "D")

def subset(s,ans,index,sub):
    
    if index==len(s):
        if len(ans)==0:
            sub.append("null")
        else:
            sub.append(ans)
        return
    subset(s, ans+s[index], index+1,sub)
    subset(s, ans, index+1,sub)
s=input("enter the number") 
sub=[]

subset(s,"", 0,sub)
print(sub)
'''

def bactracking(l,index,value):
    
    if index==len(l):
        return
    l[index]=value
    bactracking(l, index+1, value+5)#../recusrion
    l[index]=value #backtracking..

l=[0,0,0,0,0]
print(l)
bactracking(l, 0, value=10)
print(l) 


























