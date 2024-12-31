# Google Question
# Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# It should return 2

# Given an array = [2, 1, 1, 2, 3, 5, 2, 4]
# It should return 1

# Given an array = [2, 3, 4, 5]:
# It should return undefined

print("Approach 1")
# Approach: Naive
 
def firstRecurringCharacter(nums):
    recurring_pairs = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                recurring_pairs.append([i, j])

    # print("Recurring pairs: ", recurring_pairs)
    
    least_j_value = +float('inf')

    if len(recurring_pairs) > 0:
        for i in range(len(recurring_pairs) - 1):
            min_value = min(recurring_pairs[i][1], recurring_pairs[i+1][1])
            if min_value < least_j_value:
                least_j_value = min_value

    # print("least j value", least_j_value)
    
    for i in range(len(recurring_pairs)):
        if recurring_pairs[i][1] == least_j_value:
            return nums[recurring_pairs[i][1]]
    
    return None

array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
print(firstRecurringCharacter(array))

array = [2, 1, 1, 2, 3, 5, 2, 4]
print(firstRecurringCharacter(array))

array = [2, 3, 4, 5]
print(firstRecurringCharacter(array))

print("Approach 2")

# Approach: Hash Table
def firstRecurringCharacter1(nums):
    visited_elements = {}

    for i in range(len(nums)):
        if nums[i] in visited_elements:
            return nums[i]
        visited_elements[nums[i]] = True
    
    return None


array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
print(firstRecurringCharacter1(array))

array = [2, 1, 1, 2, 3, 5, 2, 4]
print(firstRecurringCharacter1(array))

array = [2, 3, 4, 5]
print(firstRecurringCharacter1(array))

"""
Hash Table

### **Time Complexity**
- **Outer Loop:** The loop iterates over the entire list `nums`, which has \( n \) elements. Therefore, the loop runs \( O(n) \) times.
- **Dictionary Operations:**
  - The `in` operation to check if `nums[i]` exists in `visited_elements` has an average time complexity of \( O(1) \), because Python's dictionary is implemented as a hash table.
  - Assigning `visited_elements[nums[i]] = True` also has an average time complexity of \( O(1) \).

Overall, the time complexity is **\( O(n) \)**.

---

### **Space Complexity**
- **Dictionary:** The `visited_elements` dictionary can hold up to \( n \) entries in the worst case, where all elements in `nums` are unique. Each entry consumes \( O(1) \) space, so the total space used by the dictionary is \( O(n) \).
- **Other Variables:** Fixed-size variables such as `i` and `nums[i]` occupy constant space, \( O(1) \).

Overall, the space complexity is **\( O(n) \)**.

---

### **Summary**
- **Time Complexity:** \( O(n) \)
- **Space Complexity:** \( O(n) \)
"""