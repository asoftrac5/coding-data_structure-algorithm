# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def moveZeroesAtTheEnd(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums[i])
            nums.remove(nums[i])
    return nums

nums = [0,1,0,3,12]
print(moveZeroesAtTheEnd(nums))


def moveZeroesAtTheEndOfArray(nums):
    zero_count = nums.count(0)

    nums[:] = [num for num in nums if num != 0]
    nums.extend([0] * zero_count)

    return nums

nums = [0,1,0,3,12]
print(moveZeroesAtTheEndOfArray(nums))