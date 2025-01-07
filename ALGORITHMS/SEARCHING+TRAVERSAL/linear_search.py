# example

beasts = ['Centaur', 'Godzilla', 'Mosura', 'Minotaur', 'Hydra', 'Nessie']

print(beasts.index('Godzilla'))

# """
# ### **Important Notes: Linear Search**

# 1. **Definition:**
#    - **Linear Search** (or Sequential Search) is a method of finding a target value in a list.
#    - It involves checking each element of the list one by one until:
#      - A match is found.
#      - Or all elements are checked (target not found).

# 2. **Process:**
#    - Starts from the first element and proceeds sequentially.
#    - Example:
#      - Checking the first item, then the second, and so on.

# 3. **Best and Worst Cases:**
#    - **Best Case:** \( O(1) \) time, if the target is the first element.
#    - **Worst Case:** \( O(n) \), if the target is at the end or not present.

# 4. **Use Cases and Examples:**
#    - Example list: `["ant", "bat", "Godzilla", "dragon"]`
#    - Searching for "Godzilla":
#      - **JavaScript Implementations:**
#        - **`indexOf`**: Returns the index (e.g., `1` for "Godzilla").
#        - **`findIndex`**: Takes a function condition and returns the index.
#        - **`find`**: Takes a function and returns the element itself.
#        - **`includes`**: Returns `true` or `false` if the item exists.

# 5. **Performance:**
#    - Linear search has **linear time complexity \( O(n) \)**.
#    - It is **not efficient for large datasets** as the list size grows.
#    - Unsuitable for tasks like indexing websites (e.g., Google) or searching large social networks (e.g., Facebook).

# 6. **Limitations:**
#    - **Inefficient for large datasets:** Requires checking every element.
#    - Cannot leverage sorted data for optimization.

# 7. **Key Question:**
#    - Can we optimize searching if the list is **sorted**? 
#    - Sorting opens opportunities for faster search methods, as discussed in the next section.

# **Takeaway:**
# Linear search is simple but inefficient for large datasets due to its \( O(n) \) time complexity. Optimization is possible with sorted data, enabling faster algorithms like binary search.
# """