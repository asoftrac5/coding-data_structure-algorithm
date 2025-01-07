numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def quickSort(array, left, right):
    pivot = None
    partitionIndex = None

    if left < right:
        pivot = right

        partitionIndex = partition(array, pivot, left, right)

        # Sort left and right arrays
        quickSort(array, left, partitionIndex - 1)
        quickSort(array, partitionIndex + 1, right)

    return array

def partition(array, pivot, left, right):
    pivotValue = array[pivot]
    partitionIndex = left

    for i in range(left, right):
        if array[i] < pivotValue:
            swap(array, i, partitionIndex)
            partitionIndex += 1

    swap(array, right, partitionIndex)
    return partitionIndex

def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp


answer = quickSort(numbers, 0, len(numbers) - 1)
print(answer)





































"""
def quickSort(array, left, right):
    arr_len = len(array)
    pivot = None
    partitionIndex = None
    
    if left < right:
        pivot = right
        partitionIndex = partition(array, pivot, left, right)

        # sort left and right
        quickSort(array, left, partitionIndex - 1)
        quickSort(array, partitionIndex + 1, right)

    return array

def partition(array, pivot, left, right):
    pivotValue = array[pivot]
    partitionIndex = left

    for i in range(left, right):
        if array[i] < pivotValue:
            swap(array, i, partitionIndex)
            partitionIndex += 1
    swap(array, right, partitionIndex)
    return partitionIndex
    
def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp

# Select first and last index as 2nd and 3rd parameters
answer = quickSort(numbers, 0, len(numbers) - 1)
print(answer)

"""