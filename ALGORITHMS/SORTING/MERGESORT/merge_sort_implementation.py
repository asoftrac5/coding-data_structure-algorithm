numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def mergeSort(array):
    if len(array) == 1:
        return array
    
    # Split the array into left and right
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Recursively sort the left and right arrays
    left = mergeSort(left)
    right = mergeSort(right)

    # Merge the sorted left and right arrays
    return merge(left, right)

def merge(left, right):
    left_index = 0
    right_index = 0
    result = []

    # Merge the arrays while maintaing the order of the elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


answer = mergeSort(numbers)
print(answer)






































"""
    if len(array) <= 1:
        return array
    
    # Split array into right and left
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Recursively sort both halves
    left = mergeSort(left)
    right = mergeSort(right)

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    # Merge the two arrays while maintaining order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right array
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result
"""