def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = 0
    start = end = temp_start = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1
    
    return nums[start : end + 1]

nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums1))

# i = 0: cu_sum = 0, ts = 1
# i = 1: cu_sum = 1, max = 1, start = 1, end = 1
# i = 2: cu_sum = 0, ts = 3
# i = 3: cu_sum = 4, max = 4, start = 3, end = 3
# i = 4: cu_sum = 3, 
# i = 5: cu_sum = 5, max = 5, start = 3, end = 5
# i = 6: cu_sum = 6, max = 6, start = 3, end = 6
# i = 7: cu_sum = 1,
# i = 8: cu_sum = 5

# nums[3:7]
# [4, -1, 2, 1]