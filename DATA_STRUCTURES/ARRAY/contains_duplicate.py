# Approach 1
def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

nums = [1, 2, 3, 1]
print(containsDuplicate(nums))

nums = [1,2,3,4]
print(containsDuplicate(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))

print('\n')

# Approach 2
def containsDuplicate1(nums):
    if len(set(nums)) == len(nums):
        return False
    return True
    
nums = [1, 2, 3, 1]
print(containsDuplicate1(nums))

nums = [1,2,3,4]
print(containsDuplicate1(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate1(nums))

print('\n')

# Approach 3
def containsDuplicate2(nums):
    look_up = {}

    for num in nums:
        if num in look_up:
            return True
        else:
            look_up[num] = True
    
    return False

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate2(nums))

print('\n')

# Approach 4
def containsDuplicate3(nums):
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    
    return False

nums = [1, 2, 3, 1]
print(containsDuplicate3(nums))

nums = [1,2,3,4]
print(containsDuplicate3(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate3(nums))

print('\n')

# Approach 5

def containsDuplicate4(nums):
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        else:
            num_set.add(num)

    return False

nums = [1, 2, 3, 1]
print(containsDuplicate4(nums))

nums = [1,2,3,4]
print(containsDuplicate4(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate4(nums))