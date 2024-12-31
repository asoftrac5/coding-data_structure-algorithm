# # merge the given two sorted arrays
# # Approach 1
array1 = [0, 3, 4, 31]
array2 = [4, 6, 30]
# def mergeSortedArrays(a1, a2):
#     # Check input
#     if len(a1) == 0:
#         return a2
    
#     if len(a2) == 0:
#         return a1
    
#     sorted_array = []
#     i, j = 0, 0
#     while i < len(a1) and j < len(a2):
#         if a1[i] < a2[j]:
#             sorted_array.append(a1[i])
#             i += 1
#         else:
#             sorted_array.append(a2[j])
#             j += 1
#     while i < len(a1):
#         sorted_array.append(a1[i])
#         i += 1
#     while j < len(a2):
#         sorted_array.append(a2[j])
#         j += 1
#     return sorted_array

# print(mergeSortedArrays(array1, array2))

# # Approach 2
# def mergeSortedArrays1(a1, a2):
#     sorted_array = []

#     merged_array = a1 + a2

#     while len(merged_array) > 0:
#         least_value = min(merged_array)
#         merged_array.remove(least_value)
#         sorted_array.append(least_value) 

#     return sorted_array

# print(mergeSortedArrays1(array1, array2))

def mergeSortedArrays(a1, a2):
    # Check for inputs
    if not a1:
        return a2
    if not a2:
        return a1
    
    merge_sorted_array = []

    i, j = 0, 0

    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            merge_sorted_array.append(a1[i])
            i += 1

        else:
            merge_sorted_array.append(a2[j])
            j += 1

    while i < len(a1):
        merge_sorted_array.append(a1[i])
        i += 1

    while j < len(a2):
        merge_sorted_array.append(a2[j])
        j += 1

    return merge_sorted_array

print(mergeSortedArrays(array1, array2))