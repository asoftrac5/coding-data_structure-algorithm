# Given 2 arrays, create a function that lets a user know (true/false) whether these two arrays contain any common items

# For example:
# array1 = ['a', 'b', 'c', 'x']
# array2 = ['z', 'y', 'i']
# Should return false

# array1 = ['a', 'b', 'c', 'x']
# array2 = ['z', 'y', 'x']
# Should return true

# 2 parameters - arrays - no size limit
# return true or false

# Bruteforce approach - O(n^2)
def containsCommonItems(a1, a2): # O(a * b)
    for i in a1:
        for j in a2:
            if i == j:
                return True
    
    return False

# array1 = ['a', 'b', 'c', 'x']
# array2 = ['z', 'y', 'x']

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i']

# space complexity - O(1) - no new variable is created
print(containsCommonItems(array1, array2))

# Efficient improved approach
def containsCommonItems2(a1, a2):
    a3 = a1 + a2
    a3 = set(a3)
    
    if len(a3) == (len(a1) + len(a2)):
        return False
    else:
        return True
    
array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'a']

print(containsCommonItems2(array1, array2))


# Given 2 arrays, create a function that lets a user know (true/false) whether these two arrays contain any common items

# For example:
# array1 = ['a', 'b', 'c', 'x']
# array2 = ['z', 'y', 'i']
# Should return false

# array1 = ['a', 'b', 'c', 'x']
# array2 = ['z', 'y', 'x']
# Should return true

# 2 parameters - arrays - no size limit
# return true or false

# Better approach - O(a + b)

# More efficient approach
def containsCommonItems3(a1, a2):
    a1_hash = {}
    for item in a1:
        a1_hash[item] = True

    print(f"keys are: {a1_hash.keys()}")

    for j in a2:
        if j in a1_hash:
            return True
        
    return False

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i']
print(containsCommonItems3(array1, array2))

print("Approach 4:")
def containsCommonItems4(a1, a2):
    # Loop through first array and create object where properties == items in the array
    
    if a1 is None or a2 is None:
        return False
    
    a1_hash = {}
    for i in a1:
        if not a1_hash.get(i):
            a1_hash[i] = True

    # Loop through second array and check if item in second array exist on created objects
    for j in a2:
        if a1_hash.get(j):
            return True
    
    return False

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i']
# Time complexity - O(a + b)
# Space complexity - O(a)
print(containsCommonItems4(array1, None))

# Can we assume always 2 parameters
# What if the arrays are null
