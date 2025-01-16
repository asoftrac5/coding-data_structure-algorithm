calculations = 0

def fibonacci(n): # O(2^n)
    global calculations
    calculations += 1
    if n < 2:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Normal: ", fibonacci(35))
print("Normal No of Calculations: ", calculations)

m_calculations = 0
def fibonacciMaster():
    cache = {}
    def fib(n):
        global m_calculations
        m_calculations += 1
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fib(n - 1) + fib(n - 2)
                return cache[n]
            
    return fib

fasterFib = fibonacciMaster()
print("DP: ", fasterFib(35))
print("DP No of Calculations: ", m_calculations)

def fibonacciMaster2(n):
    answer = [0, 1]

    for i in range(2, n + 1):
        answer.append(answer[i - 2] + answer[i - 1])
    return answer.pop()

print("DP2: ", fibonacciMaster2(35))
# print("DP No of Calculations: ", m_calculations)

"""
### Important Notes on Dynamic Programming and Optimization Approaches

1. **Dynamic Programming Overview**:
   - **Key Question to Identify DP Problems**:
     1. Can the problem be divided into smaller subproblems (recursion-based)?
     2. Are there repetitive subproblems or tasks?
     3. If yes, use **memoization** to cache results and avoid redundant calculations.

2. **Memoization (Top-Down Approach)**:
   - Focuses on solving the problem recursively while caching results of previously computed subproblems.
   - Advantages:
     - Intuitive for recursive problems.
     - Easy to implement for problems like Fibonacci.
   - Disadvantage:
     - May involve more function call overhead compared to the bottom-up approach.

3. **Bottom-Up Approach**:
   - Starts from the simplest base cases and iteratively builds up to solve the larger problem.
   - Example: Iterative Fibonacci Implementation:
     - Initialize a list with base values \( [0, 1] \).
     - Use a loop to calculate subsequent values using previously computed results.
     - Time Complexity: \( O(n) \), Space Complexity: \( O(1) \) (if only two variables are used).
   - Advantages:
     - Avoids recursion entirely.
     - Can be more efficient in terms of function call overhead.
   - Disadvantages:
     - May be harder to visualize and implement for complex problems.

4. **Comparison: Top-Down vs. Bottom-Up**:
   - **Top-Down**:
     - Recursive, uses memoization.
     - Easier to implement and understand for certain problems.
   - **Bottom-Up**:
     - Iterative, builds solutions step-by-step.
     - More efficient in reducing stack memory usage but harder to recognize when applicable.

5. **General Takeaways**:
   - Dynamic programming helps optimize problems by avoiding repeated computations.
   - Recognizing repetitive subproblems and caching their results can significantly reduce time complexity.
   - Both approaches are valid, and the choice depends on problem requirements and personal preference.
   - Interviews typically focus on one method; rarely are both required.

6. **Power of Dynamic Programming**:
   - Saves computational resources by minimizing redundant work.
   - Highlights the importance of understanding program execution and optimization.
   - Mastering these techniques is a hallmark of a skilled engineer.
"""