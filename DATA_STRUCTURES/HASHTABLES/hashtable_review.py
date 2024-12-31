"""
### Important Notes on Hash Tables

1. **Significance of Hash Tables in Interviews:**
   - Hash tables are frequently used in interview questions to optimize nested loops (O(n²)) into linear time (O(n)).
   - Recognizing this pattern is invaluable for solving problems efficiently during interviews.

2. **Key Properties of Hash Tables:**
   - **Fast Lookups:** O(1) on average.
   - **Fast Inserts:** O(1) on average.
   - **Flexible Keys:** Allows custom keys instead of fixed numeric indexes like arrays.
   - **Collision Resolution:** Handled by the underlying language, though worst-case scenarios can degrade performance.

3. **Downsides of Hash Tables:**
   - **Unordered:** Data in hash tables lacks a defined order.
   - **Slow Key Iteration:** Retrieving all keys can be slow as it involves scanning the memory space.
   - **Collision Impact:** Can lead to O(mn) operations in the worst case, though rare.

4. **Practical Usage of Hash Tables:**
   - Often used to optimize **time complexity** by reducing nested loops.
   - In exercises, hash tables helped identify common elements between arrays, reducing time complexity from O(a × b) to O(a + b).

5. **Trade-offs of Hash Tables:**
   - **Time vs. Space:** Faster access times often come at the cost of increased space complexity.
   - Using hash tables may require extra memory to store state, resulting in a space complexity of O(m + n).

6. **Design Principles in Hash Table Usage:**
   - **Modular Code:** Writing maintainable and testable code using hash tables.
   - **Avoid Repetition:** Following DRY (Don't Repeat Yourself) principles.
   - **Good Data Structure Selection:** Choosing hash tables over arrays or other structures based on the problem.

7. **Heuristics and Interview Tricks:**
   - Hash tables are often the go-to solution for optimizing code with high time complexity.
   - Using hash tables to store additional state can lead to significant runtime improvements.

8. **Space-Time Trade-offs:**
   - Hash tables highlight the trade-off where additional memory usage results in better runtime performance.

9. **Applications Beyond Basics:**
   - Hash tables will be revisited in topics like **dynamic programming** and other advanced data structures.

10. **Progress Checklist:**
    - **Crossed Off Topics:** Hash tables and some heuristics for interviews.
    - **Learning Goals:** Understanding data structures, code readability, modularity, and space-time trade-offs.

11. **Encouragement:**
    - Hash tables and arrays are foundational data structures that will be used to learn others.
    - Take breaks and enjoy the learning journey!
"""