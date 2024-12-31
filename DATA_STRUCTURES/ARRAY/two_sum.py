# Approach 1
def two_sum(ar, target):
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if ar[i] + ar[j] == target:
                return i, j
            j += 1
        i += 1
    
    return None

num = [2, 7, 11, 15]
target = 9
print(two_sum(num, target))

num = [3, 2, 4]
target = 6
print(two_sum(num, target))

num = [3, 3]
target = 6
print(two_sum(num, target))

# Approac 2

def two_sum1(ar, target):
    complement = {}

    for i in range(len(ar)):
        if ar[i] in complement:
            return complement[ar[i]], i
        complement[target - ar[i]] = i
            
        
num = [2, 7, 11, 15]
target = 9
print(two_sum1(num, target))

num = [3, 2, 4]
target = 6
print(two_sum1(num, target))

num = [3, 3]
target = 6
print(two_sum1(num, target))

# Approac 3

def two_sum2(ar, target):
    pair_idx = {}

    for i, num in enumerate(ar):
        if target - num in pair_idx:
            return [pair_idx[target - num], i]
        pair_idx[num] = i
            
        
num = [2, 7, 11, 15]
target = 9
print(two_sum2(num, target))

num = [3, 2, 4]
target = 6
print(two_sum2(num, target))

num = [3, 3]
target = 6
print(two_sum2(num, target))