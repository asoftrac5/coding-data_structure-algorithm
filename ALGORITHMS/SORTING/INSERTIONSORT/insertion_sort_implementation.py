numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertionSort(array):
    for i in range(len(array)):
        if array[i] < array[0]:
            # move the element to the first position in the array
            array.insert(0, array.pop(i))
        else:
            # find where the element should be placed in the array
            for j in range(i):
                if array[i] > array[j - 1] and array[i] < array[j]:
                    # move the element to the right spot
                    array.insert(j, array.pop(i))

    return array

insertionSort(numbers)
print(numbers)