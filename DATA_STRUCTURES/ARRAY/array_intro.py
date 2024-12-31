strings = ['a', 'b', 'c', 'd']

# 4 * 4 = 16 bytes of storage

# Access an element from the array
print(strings[2])

# append - O(1)
strings.append('e')
print(strings)

# pop - O(1)
strings.pop() 
print(strings)

# insert an element in the beginning of the array - O(n)
strings.insert(0, 'x')
print(strings)

# insert an element in the middle of the array - O(n)
strings.insert(2, "n")
print(strings)

# delete an element - O(n)
strings.remove('a')
print(strings)