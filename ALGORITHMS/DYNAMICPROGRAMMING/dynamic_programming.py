"""
### Important Notes on Optimizing Fibonacci with Dynamic Programming

1. **Problem with Recursive Fibonacci**:
   - Recursive Fibonacci suffers from **repeated calculations**:
     - For \( F(7) \), Fibonacci(1) is calculated 5 times, Fibonacci(2) multiple times, and so on.
     - This overlap leads to redundant computations, making the algorithm highly inefficient.
   - Recursive Fibonacci has a time complexity of \( O(2^n) \), resulting in exponential growth in calculations as \( n \) increases.

2. **Dynamic Programming Optimization**:
   - **Memoization** is used to optimize recursion by storing results of subproblems in a cache:
     - When a value is calculated, it is stored.
     - If the same calculation is needed later, the cached result is used instead of recalculating.
   - This approach transforms the time complexity from \( O(2^n) \) to \( O(n) \), drastically improving efficiency.

3. **Steps to Implement Dynamic Programming**:
   - Combine **divide-and-conquer** with **reuse** through caching:
     - Break the problem into subproblems (e.g., Fibonacci tree structure).
     - Reuse results of repetitive subproblems.
   - **Steps to Identify DP Problems**:
     1. **Subproblem Identification**: Can the problem be divided into smaller subproblems?
     2. **Repetition**: Are the subproblems repetitive (calculated multiple times)?
     3. **Cache Potential**: Can results of subproblems be cached for reuse?
     4. **Optimization**: Use a table (e.g., hash table) to store and retrieve precomputed results.

4. **Benefits of Dynamic Programming**:
   - Reduces redundant calculations.
   - Improves both **time complexity** and **space complexity**.
   - Widely applicable to problems with overlapping subproblems and optimal substructure.

5. **General Approach to DP**:
   - Recognize the problem’s recursive structure.
   - Check for repetitive subproblems.
   - Implement caching to optimize calculations.

6. **Practical Advice**:
   - Dynamic programming is not limited to Fibonacci but applies to many computational problems.
   - Follow the outlined pattern to identify and apply DP techniques in real-world scenarios.

7. **Next Steps**:
   - Implement memoization for Fibonacci to improve its performance.
   - Practice with similar problems to solidify understanding of dynamic programming.
"""