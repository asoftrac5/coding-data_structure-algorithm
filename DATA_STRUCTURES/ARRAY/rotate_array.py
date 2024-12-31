# Approach 1

def rotateArray(nums, k):
    for _ in range(k):
        cur_num = nums.pop()
        nums.insert(0, cur_num)
    return nums

nums = [1,2,3,4,5,6,7]
k = 3

print(rotateArray(nums, k))

# Approach 2

def rotateArray2(nums, k):
    # 1. Reverse the whole array
    nums.reverse()

    # 2. Reverse the first k elements
    nums[:k] = reversed(nums[:k])

    # 3. Reverse the remaining elements
    nums[k:] = reversed(nums[k:])
    
    return nums

nums = [1,2,3,4,5,6,7]
print(rotateArray2(nums, 3))