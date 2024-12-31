import time


# nemo = ['nemo']
# everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
# large = ['nemo'] * 1000000

# def find_nemo(array):

#     # t0 = time.time()
#     for i in range(len(array)):
#         if array[i] == 'nemo':
#             print('Found Nemo!')

#     t1 = time.time()
#     # print(f'Time taken: { t1 - t0} milliseconds')

# find_nemo(large) # O(n) --> Linear Time



boxes = [0, 1, 2, 3, 4, 5]

def printFirstTwoBoxes(boxes):
    print(boxes[0]) # O(1)
    print(boxes[1]) # O(1)

printFirstTwoBoxes(boxes) # O(2)

# No matter what is the number of elements, but if it is a contant then it is considered contant time of O(1)
# O(1) - Constant Time