# Just
# cache = {}
# def memoizedAddTo80(n):
#     if (n in cache):
#         return cache[n]
#     else:
#         print("Long Time")
#         cache[n] = n + 80
#         return cache[n]

# print("1",memoizedAddTo80(5))
# print("2", memoizedAddTo80(5))


def memoizedAddTo80():
    cache = {}

    def memoized(n):
        if (n in cache):
            return cache[n]
        else:
            print("Long Time")
            cache[n] = n + 80
            return cache[n]
    return memoized

memoized = memoizedAddTo80()

print("1",memoized(5))
print("2", memoized(6))

"""
### Important Notes on Dynamic Programming: Caching and Memorization in Python

#### **1. Overview of Dynamic Programming (DP)**
- **Definition**:
  - DP is an **optimization technique** used to solve complex problems by breaking them down into simpler subproblems.
  - It involves **solving each subproblem once** and **storing their solutions** to avoid redundant computations.
  
- **Core Concepts**:
  - **Caching**: Storing computed values for future use.
  - **Memorization**: A specific form of caching where function results are stored based on input parameters.

#### **2. Understanding Caching**
- **Definition**:
  - Caching is a method to **store values** so they can be **retrieved quickly** later, enhancing program efficiency.
  
- **Analogy**:
  - Think of caching as carrying a **backpack** to school with essential items (like pencils) readily available, avoiding the need to go back home repeatedly.

- **Purpose**:
  - **Speed Up Programs**: By reusing previously computed results.
  - **Reduce Redundant Calculations**: Saves time and computational resources, especially for expensive operations.

#### **3. Memorization in Dynamic Programming**
- **Definition**:
  - **Memorization** is a technique where the results of function calls are **stored based on their input parameters**.
  
- **How It Works**:
  1. **First Call**:
     - Check if the input exists in the cache.
     - If not, compute the result, store it in the cache, and return the value.
  2. **Subsequent Calls**:
     - If the input exists in the cache, **retrieve and return** the cached value without recomputing.

- **Example Concept**:
  - **Function Without Caching**:
    ```python
    def add_to_80(n):
        return n + 80

    print(add_to_80(5))  # Output: 85
    print(add_to_80(5))  # Output: 85 (recomputed)
    ```
  - **Function With Memorization**:
    ```python
    cache = {}

    def memoized_add_to_80(n):
        if n in cache:
            return cache[n]
        else:
            print("Long Time")  # Simulate an expensive computation
            cache[n] = n + 80
            return cache[n]

    print(memoized_add_to_80(5))  # Output: Long Time \n 85
    print(memoized_add_to_80(5))  # Output: 85 (retrieved from cache)
    ```

#### **4. Improving Caching Practices in Python**
- **Avoid Global Scope for Cache**:
  - **Issue**: Using a global cache (e.g., `cache = {}` outside the function) can lead to **namespace pollution** and **unintended side effects**.
  - **Solution**: Encapsulate the cache within the function scope.

- **Python Techniques for Encapsulated Caching**:
  1. **Using Default Mutable Arguments**:
     ```python
     def memoized_add_to_80(n, cache={}):
         if n in cache:
             return cache[n]
         else:
             print("Long Time")
             cache[n] = n + 80
             return cache[n]

     print(memoized_add_to_80(5))  # Output: Long Time \n 85
     print(memoized_add_to_80(5))  # Output: 85
     ```
  
  2. **Using Closures**:
     ```python
     def create_memoized_add_to_80():
         cache = {}
         def memoized(n):
             if n in cache:
                 return cache[n]
             else:
                 print("Long Time")
                 cache[n] = n + 80
                 return cache[n]
         return memoized

     memoized_add_to_80 = create_memoized_add_to_80()
     print(memoized_add_to_80(5))  # Output: Long Time \n 85
     print(memoized_add_to_80(5))  # Output: 85
     ```

  3. **Using Decorators (`functools.lru_cache`)**:
     - **Advantages**:
       - Simplifies memoization without manual cache management.
       - Provides built-in cache size limits and eviction policies.
     - **Example**:
       ```python
       from functools import lru_cache

       @lru_cache(maxsize=None)
       def memoized_add_to_80(n):
           print("Long Time")
           return n + 80

       print(memoized_add_to_80(5))  # Output: Long Time \n 85
       print(memoized_add_to_80(5))  # Output: 85
       ```

#### **5. Best Practices for Caching and Memorization**
- **Encapsulate the Cache**:
  - Keep the cache within the function to prevent global namespace pollution.
  - Use closures or decorators to manage the cache efficiently.
  
- **Choose Appropriate Caching Strategy**:
  - **Simple Functions**: Default mutable arguments or closures.
  - **Complex Functions**: Decorators like `@lru_cache` for automatic caching.

- **Understand When to Use Memoization**:
  - Problems with **overlapping subproblems** and **optimal substructure**.
  - Scenarios where **repeated computations** occur with the same inputs.

#### **6. Advantages of Proper Caching and Memorization**
- **Efficiency**:
  - Reduces computation time by avoiding redundant calculations.
  - Enhances performance, especially for functions with expensive operations.
  
- **Scalability**:
  - Makes algorithms more scalable by optimizing repeated operations.

- **Simplicity**:
  - Encapsulating caching logic keeps functions clean and focused on their primary tasks.

#### **7. Considerations and Limitations**
- **Cache Size**:
  - Be mindful of memory usage, especially with large caches.
  - Use decorators like `@lru_cache` to manage cache size automatically.
  
- **Cache Invalidation**:
  - Ensure that cached results remain valid, especially in dynamic environments where inputs may change.

- **Recursion Depth**:
  - Deep recursive calls can lead to stack overflow; iterative approaches with explicit stacks can mitigate this.

#### **8. Interview Tips**
- **Understand the Concept**:
  - Be able to explain what dynamic programming and memoization are.
  - Know the difference between caching in global scope vs. function scope.
  
- **Know Implementation Techniques**:
  - Familiarize yourself with Python-specific memoization methods (default arguments, closures, decorators).
  
- **Explain Benefits and Trade-offs**:
  - Highlight how memoization optimizes performance.
  - Discuss memory considerations and how different techniques handle caching.

- **Prepare for Variations**:
  - Be ready to implement simple memoization manually or use built-in decorators like `@lru_cache`.

#### **Example Summary in Python**
- **Manual Memorization with Default Arguments**:
  ```python
  def memoized_add_to_80(n, cache={}):
      if n in cache:
          return cache[n]
      else:
          print("Long Time")
          cache[n] = n + 80
          return cache[n]

  print(memoized_add_to_80(5))  # Output: Long Time \n 85
  print(memoized_add_to_80(5))  # Output: 85
  ```

- **Using a Closure**:
  ```python
  def create_memoized_add_to_80():
      cache = {}
      def memoized(n):
          if n in cache:
              return cache[n]
          else:
              print("Long Time")
              cache[n] = n + 80
              return cache[n]
      return memoized

  memoized_add_to_80 = create_memoized_add_to_80()
  print(memoized_add_to_80(5))  # Output: Long Time \n 85
  print(memoized_add_to_80(5))  # Output: 85
  ```

- **Using `functools.lru_cache` Decorator**:
  ```python
  from functools import lru_cache

  @lru_cache(maxsize=None)
  def memoized_add_to_80(n):
      print("Long Time")
      return n + 80

  print(memoized_add_to_80(5))  # Output: Long Time \n 85
  print(memoized_add_to_80(5))  # Output: 85
  ```

### **Conclusion**
- **Dynamic Programming** leverages **caching** and **memorization** to optimize problem-solving.
- In Python, **encapsulating the cache** within functions using **default arguments**, **closures**, or **decorators** is essential for clean and efficient code.
- Understanding and applying these techniques enhances your ability to write performant programs and prepares you for technical interviews.
"""


# Different methods to convert the cache from global scope to function scope
print("Global scope: ")
cache = {}
def memoizedAddTo80(n):
    if n in cache:
        return cache[n]
    else:
        print("Long Time")
        cache[n] = n + 80
        return cache[n]

print("1", memoizedAddTo80(5))
print("2", memoizedAddTo80(5))

# Using default agument parameters
print("Using Arguemtn Parameter: ")
def memoizedAddTo80UsingArgumentParameter(n, cache = {}):
    if n in cache:
        return cache[n]
    else:
        print("Long Time")
        cache[n] = n + 80
        return cache[n]
    
print("1", memoizedAddTo80UsingArgumentParameter(5))
print("2", memoizedAddTo80UsingArgumentParameter(5))

# Using function tools
print("Using function tools: ")
from functools import lru_cache
@lru_cache(maxsize=None)
def memoizedAddTo80UsingLruCache(n):
    cache[n] = n + 80
    return cache[n]
    
print("1", memoizedAddTo80UsingLruCache(5))
print("2", memoizedAddTo80UsingLruCache(5))