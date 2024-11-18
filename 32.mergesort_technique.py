# self coded code but added comments using G.P.T
#-------------------------------------------------------#

# Merge Sort function
def merge_sort(L, lindex, rindex):
    # If the subarray has more than one element, continue splitting
    if lindex < rindex:
        # Find the middle index to divide the list into two halves
        mid = (lindex + rindex) // 2
        
        # Recursively sort the left half of the array
        merge_sort(L, lindex, mid)
        
        # Recursively sort the right half of the array
        merge_sort(L, mid + 1, rindex)
        
        # Merge the sorted halves
        mergefun(L, lindex, mid, rindex)

# Merge function to combine two sorted halves
def mergefun(L, low, mid, high):
    # Create temporary arrays for the left and right subarrays
    left_arr = L[low:mid + 1]
    right_arr = L[mid + 1:high + 1]
    
    # Initialize pointers for left, right subarrays, and the main array
    i = 0  # Pointer for the left subarray
    j = 0  # Pointer for the right subarray
    k = low # Pointer for the main array where the merged result will be placed
    
    # Merge the two sorted subarrays into the main array
    while i < len(left_arr) and j < len(right_arr):
        # Compare elements from both subarrays and place the smaller one into the main array
        if left_arr[i] < right_arr[j]:
            L[k] = left_arr[i]  # Place the element from the left array into L
            i += 1  # Move the pointer in the left array forward
        else:
            L[k] = right_arr[j]  # Place the element from the right array into L
            j += 1  # Move the pointer in the right array forward
        k += 1  # Move the pointer in the main array forward

    # If there are remaining elements in the left subarray, add them to the main array
    while i < len(left_arr):
        L[k] = left_arr[i]  # Place the remaining elements from the left array into L
        i += 1  # Move the pointer in the left array forward
        k += 1  # Move the pointer in the main array forward

    # If there are remaining elements in the right subarray, add them to the main array
    while j < len(right_arr):
        L[k] = right_arr[j]  # Place the remaining elements from the right array into L
        j += 1  # Move the pointer in the right array forward
        k += 1  # Move the pointer in the main array forward

# Test the merge_sort function with an example list
L = [23, 4, 5, 53, 12, 21, 6, 7]

# Print the list before sorting
print("Before sorting:", L)

# Call the merge_sort function to sort the list
merge_sort(L, 0, len(L) - 1)

# Print the list after sorting
print("After sorting:", L)
