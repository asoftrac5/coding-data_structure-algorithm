# Given a number N return the index value of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# The pattern of the sequence is that each value is the sum of the 2 previous values, that 
# means that for N = 5 -> 2 + 3

# Question: Given n = index of the sequence, return the value associated with the sequence index

def fibonacciIterative(n): # O(n)
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i - 2] + arr[i - 1])
    
    return arr[n]

print("Iterative: ")
print(fibonacciIterative(10))

print("\n")

def fibonacciRecursive(n): # O(2^n)
    # Base case:
    if n < 2:
        return n
    
    # Recursive case
    return fibonacciIterative(n - 2) + fibonacciIterative(n - 1)

print("Recursive: ")
print(fibonacciRecursive(10))

"""
### Key Notes on Recursive and Iterative Fibonacci Functions

#### **Recursive Fibonacci Function**
1. **Base Case**: 
   - If \( n \) is less than 2, return \( n \) directly.
     - \( fib(0) = 0 \), \( fib(1) = 1 \).
2. **Recursive Case**:
   - Return \( fib(n-1) + fib(n-2) \), which calculates the sum of the two previous Fibonacci numbers.
3. **Behavior**:
   - Recursively breaks the problem into smaller subproblems until it reaches the base case.
   - For \( fib(7) \), calls include \( fib(6) \), \( fib(5) \), and so on, creating an exponentially large tree of calculations.

4. **Example Output**:
   - \( fib(3) = 2 \), \( fib(8) = 21 \).

5. **Time Complexity**:
   - **Exponential time complexity (\( O(2^n) \))**:
     - As \( n \) increases, the number of recursive calls grows exponentially, resulting in inefficient computation for large \( n \).

6. **Limitations**:
   - Recursive approach for Fibonacci sequence leads to repeated calculations.
   - Slower as \( n \) grows, e.g., \( fib(43) \) takes significantly longer to compute.

---

#### **Iterative Fibonacci Function**
1. **Approach**:
   - Use an array initialized with the first two Fibonacci numbers: `[0, 1]`.
   - Use a loop to calculate and append the next Fibonacci numbers up to the desired index.
   - Return the value at the specified index.

2. **Logic**:
   - Start the loop at index 2, and for each iteration:
     - Push the sum of the previous two numbers to the array.
   - Output the value at index \( n \).

3. **Example Output**:
   - \( fib(3) = 2 \), \( fib(8) = 21 \).

4. **Time Complexity**:
   - **Linear time complexity (\( O(n) \))**:
     - Iterates through the loop \( n-2 \) times, making it significantly faster than the recursive approach.

---

#### **Comparison of Recursive and Iterative Approaches**
1. **Recursive Pros**:
   - Cleaner and more readable for simple problems.
   - Useful for problems with a natural recursive structure (e.g., tree traversals, divide and conquer algorithms).

2. **Recursive Cons**:
   - Inefficient for problems like Fibonacci without optimization (e.g., dynamic programming or memoization).
   - Higher risk of stack overflow for large \( n \).

3. **Iterative Pros**:
   - More efficient for Fibonacci-like problems due to lower time complexity.
   - Avoids stack overflow and redundant calculations.

4. **Iterative Cons**:
   - Code can be less intuitive or harder to read for some problems.

---

#### **Key Takeaways**
1. Recursive functions should be used when:
   - A problem can naturally be divided into subproblems (e.g., tree traversal).
   - Readability is prioritized, and performance trade-offs are acceptable.

2. Iterative solutions are preferable when:
   - Efficiency is critical, especially for simple problems like Fibonacci.

3. **Dynamic Programming & Memoization**:
   - Recursive Fibonacci can be optimized to \( O(n) \) using these techniques, reducing redundant calculations.
   - This will be discussed later in the course.

4. **Big-O Tradeoffs**:
   - Recursive Fibonacci: \( O(2^n) \) (exponential).
   - Iterative Fibonacci: \( O(n) \) (linear).

---

#### **Upcoming Topics**:
- Understanding why recursion might still be used despite inefficiencies.
- Exploring dynamic programming to optimize recursive solutions.
"""