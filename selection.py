def Selectionsort(arr):
    for i in range(len(arr)):
        min = i 

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        (arr[i], arr[min]) = (arr[min], arr[i])

arr = []
n = int(input("Enter the number of elements in the array: "))

print("Enter the elements in the array:")
for i in range(0, n):
    l = int(input())
    arr.append(l)

Selectionsort(arr)
print("The array after sorting is:")
print(arr)


















#Selection sort is a simple comparison-based sorting algorithm that divides the input array into two parts: a sorted part and an unsorted part. 

# Here's a step-by-step explanation of the selection sort algorithm:

# Start with an unsorted array of n elements.
# Find the minimum (or maximum) element in the unsorted part of the array.
# Swap the minimum (or maximum) element with the first element of the unsorted part.
# Move the boundary of the sorted part one element to the right.
# Repeat steps 2-4 until the entire array is sorted.