# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1

def search(arr, x,n ):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1

# Driver Code
arr =eval(input("enter the list:"))
x = int(input(("input to search:")))
n = len(arr)

# Function call
print(search(arr, x, n))


