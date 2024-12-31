# def booooo(n):
#     for i in range(len(n)):
#         print('boooo!')

# booooo([1, 2, 3, 4, 5]) # space complexity - O(n)

def arrayOfHiNTimes(n):
    hiArray = []

    for i in range(n):
        hiArray.append('hi')

    return hiArray

print(arrayOfHiNTimes(6)) # space complexity - O(n)