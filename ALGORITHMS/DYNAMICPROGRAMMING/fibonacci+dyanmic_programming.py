calculations = 0

def fibonacci(n): # O(2^n)
    global calculations
    calculations += 1
    if n < 2:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(20))
print("Calculations", calculations)


"""
### Important Notes on Dynamic Programming and Fibonacci Sequence

1. **Dynamic Programming Overview**:
   - Dynamic programming (DP) is essentially **caching** to optimize performance.
   - It is useful when solving problems that involve overlapping subproblems or repeated calculations.
   - The goal is to reduce computational effort by storing and reusing results.

2. **Fibonacci Sequence as an Example**:
   - Fibonacci sequence: Each number is the sum of the previous two numbers.
   - Example:
     - \( F(6) = 8 \): Calculated as \( F(5) + F(4) \).
     - \( F(7) = 13 \): Calculated as \( F(6) + F(5) \).

3. **Recursive Fibonacci Implementation**:
   - A simple recursive function for Fibonacci:
     ```python
     def fibonacci(n):
         if n < 2:
             return n
         return fibonacci(n - 1) + fibonacci(n - 2)
     ```
   - While easy to implement, it is **highly inefficient**.

4. **Efficiency of Recursive Fibonacci**:
   - Recursive Fibonacci has **exponential time complexity**: \( O(2^n) \).
   - The number of calculations grows rapidly:
     - \( F(7): 13 \) calculations.
     - \( F(8): 21 \) calculations.
     - \( F(12): 144 \) calculations.
     - \( F(20): 6,765 \) calculations.
     - \( F(30): Tens of thousands of calculations.
   - **Drawbacks**:
     - High computation time.
     - Large memory usage due to recursive function calls stacking on the call stack.

5. **Improving Efficiency with Dynamic Programming**:
   - Use **memoization** to store results of subproblems and reuse them.
   - Memoization reduces time complexity to \( O(n) \).
   - Key Idea:
     - Subproblem solutions are reused instead of recalculated.
     - This avoids redundant computation and optimizes performance.

6. **Benefits of Using Dynamic Programming**:
   - Efficient computation: Reduces exponential time complexity \( O(2^n) \) to linear time \( O(n) \).
   - Optimized memory usage: Avoids excessive recursion depth.

7. **Applications**:
   - Dynamic programming is widely applicable for problems with overlapping subproblems and optimal substructure, such as:
     - Fibonacci sequence.
     - Pathfinding (e.g., shortest path algorithms).
     - Knapsack problems.
     - Text processing (e.g., string matching).

8. **Next Steps**:
   - Explore **memoization** and its implementation.
   - Understand how to reduce both **time complexity** and **space complexity** in algorithms using DP.
"""