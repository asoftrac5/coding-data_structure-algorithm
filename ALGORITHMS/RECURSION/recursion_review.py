"""
### Important Notes on Recursion

1. **Definition of Recursion**:
   - A function that calls itself.
   - Useful for problems requiring state management across different levels of recursion.

2. **How Recursion Works**:
   - Functions are added to the call stack (like stacking glasses).
   - When reaching the base case, functions are popped from the stack in reverse order to return values.

3. **Risks of Recursion**:
   - **Stack Overflow**: Occurs when too many recursive calls exceed memory limits.
   - **Space Complexity**: Each recursive call consumes additional memory for the call stack.

4. **When to Use Recursion**:
   - Improves code readability for certain problems.
   - Suitable for problems involving **sorting** (e.g., Merge Sort, QuickSort) and **data traversal** (trees, graphs).
   - Ideal for problems requiring:
     - State preservation across calls.
     - Simpler, cleaner solutions for divide-and-conquer algorithms.

5. **Cautions**:
   - Recursive solutions can be less efficient than iterative ones.
   - Recursion and space complexity are often at odds.
   - Always weigh the pros and cons of recursion vs. iteration.

6. **Key Areas Where Recursion is Common**:
   - **Sorting algorithms**:
     - Merge Sort
     - QuickSort
   - **Tree data structures**:
     - Traversals (e.g., pre-order, in-order, post-order)
   - **Graph algorithms**:
     - Depth-first search (DFS)
   - Recursive solutions simplify the logic for such problems but require careful handling of memory.

7. **Interview Relevance**:
   - Expect questions about the trade-offs between recursion and iteration.
   - Understand recursion’s readability benefits and memory trade-offs.

8. **Best Practices**:
   - Use recursion when it simplifies code.
   - Be mindful of stack limitations and ensure a clear base case to prevent infinite recursion.

9. **Preparation for Topics Using Recursion**:
   - Sorting (Merge Sort, QuickSort).
   - Tree traversal.
   - Graph traversal.
   - Build a mental model for recognizing when recursion is appropriate. 


"""