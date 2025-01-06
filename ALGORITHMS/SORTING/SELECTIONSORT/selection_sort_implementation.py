numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(array):
    for i in range(len(array)):
        min_index = i
        temp_value = array[i]

        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        
        array[i] = array[min_index]
        array[min_index] = temp_value

    return array


selectionSort(numbers)
print(numbers)