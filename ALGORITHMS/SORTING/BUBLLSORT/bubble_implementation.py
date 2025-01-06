numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(array):
    # Code here
    # My Implementation
    # count = 0
    # while count < (len(array) + 1):
    #     for i in range(len(array)):
    #         for j in range(i+1, len(array)):
    #             if array[i] > array[j]:
    #                 temp = array[i]
    #                 array[i] = array[j]
    #                 array[j] = temp
    #             break
    #         i += 1
    #     count += 1

    # return array

    # From the course
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

bubbleSort(numbers)
print(numbers)