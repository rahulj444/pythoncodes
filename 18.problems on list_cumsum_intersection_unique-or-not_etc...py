arr = [1, 2, 3, 4, 5, 6, 7]
arr_cum = []

# Initialize the cumulative sum
cumulative_sum = 0

# Iterate through the array
for i in arr:
    cumulative_sum += i  # Add current element to cumulative sum
    arr_cum.append(cumulative_sum)  # Append the cumulative sum to the new list

print(arr_cum)

# if the list have uinque elements are not 
def uni(l):
    return len(l)==len(set(l))
print(uni([1,2,3,4,5]))


#program to find the 1st last 2nd second last so om  summ
 
def ite(l):
    leftindex = 0
    rightindex = len(l) - 1
    
    while leftindex <= rightindex:
        print(l[leftindex] + l[rightindex], end=" ")
        leftindex += 1
        rightindex -= 1

# Test list
l2 = [1, 2, 4, 5, 2, 3, 4]
ite(l2)
print()

#wave problem  [1,2,3,4,5,6,7]  ==>[1,3,2,5,4,7,6]

l=[1,2,3,4,5,6,7]
l.sort()
i=1
while i<len(l)-1:
    l[i],l[i+1]=l[i+1],l[i]
    i+=2
print(l)
    
#output:-[1, 3, 2, 5, 4, 7, 6]




    
    
    
    
    
    

    



