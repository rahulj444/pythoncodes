k = int(input("Enter the number of elements in the first set: "))
m = set(map(int, input("Enter the elements of the first set: ").split()))

j = int(input("Enter the number of elements in the second set: "))
n = set(map(int, input("Enter the elements of the second set: ").split()))

# Check if m is a subset of n or n is a subset of m using intersection
if m.intersection(n) == m or m.intersection(n) == n:
    print("True")
else:
    print("False")
