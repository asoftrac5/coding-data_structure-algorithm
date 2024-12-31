# Naive Approach
def hasPairWithSum(arr, sum):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                return True
    
    return False

num = [1, 2, 3, 4, 5]
target = 10

# print(hasPairWithSum(num, target))

# Best Approach
def hasPairWithSum2(arr, sum):
    complement = {}
    for i in arr:
        if complement.get(i):
            return True
        else:
            complement[sum - i] = True
    
    return False

num_array = [2, 4, 6, 8, 10]
sum_num = 16

# print(hasPairWithSum2(num_array, sum_num))

# Better Approach
def hasPairWithSum3(arr, sum):
    complement = set()
    for i in arr:
        if i in complement:
            return True
        else:
            complement.add(sum - i)
    
    return False

num_arr = [2, 4, 6, 8, 10]
sum_n = 17

print(hasPairWithSum2(num_arr, sum_n))