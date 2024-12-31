# Find 1st, Find nth... 

array = ['hi', 'my', 'teddy']
array[0] # O(1) - Constant Time
array[len(array) - 1] # O(1) - Constant Time


array = [
    {
        'tweet': 'hi', 
        'date': 2012
     },
    {
        'tweet': 'my', 
        'date': 2014
     },
    {
        'tweet': 'teddy', 
        'date': 2018
        }]

# O(n^2) - Quadratic Time



len('hellowmerrychristmas') # O(1) - Constant Time because the length is stored as an attribute

"""
The time complexity of the expression `len('hellowmerrychristmas')` in Python is **O(1)** (constant time).

### **Reasoning**:
1. **String Length in Python**:
   - Python strings store their length as a property internally when the string is created.
   - When you call `len()`, it simply retrieves this precomputed value.

2. **No Iteration or Processing**:
   - Unlike some operations (e.g., iterating over elements), calculating the length of a string doesn’t depend on the number of characters.
   - It’s a direct lookup, regardless of the size of the string.

### **Conclusion**:
- **Big O Notation**: **O(1)**.
- This is because the operation executes in constant time, regardless of the size of the string.
"""