def addTo80(n):
    print("It takes a long time to compute")
    return n + 80

# print(addTo80(5))
# print(addTo80(5))
# print(addTo80(5))

cache = {}
def memoizedAddTo80(n):
    if (n in cache):
        return cache[n]
    else:
        print("Long Time")
        cache[n] = n + 80
        return cache[n]

print("1",memoizedAddTo80(5))
print("2", memoizedAddTo80(5))


"""
### Important Notes on Caching and Memorization

#### **Caching**:
1. **Definition**: 
   - A way to store values temporarily so they can be reused quickly without recomputation.
   - Similar to carrying a **backpack** for quick access to essential items, avoiding repeated trips (computations).

2. **Purpose**:
   - Optimizes program efficiency by storing results of expensive operations for reuse.
   - Reduces redundant calculations, saving time and computational resources.

#### **Memorization**:
1. **Definition**: 
   - A **specific form of caching** focused on storing and reusing the results of function calls based on their **input parameters**.

2. **Key Idea**:
   - When a function is called with the same parameters:
     - If the result exists in the cache, **reuse it**.
     - If not, **compute it** and **store the result** in the cache for future use.

3. **How It Works**:
   - **First Call**:
     - Checks if the input is already in the cache.
     - If not, computes the result, stores it in the cache, and returns the value.
   - **Subsequent Calls**:
     - If the input exists in the cache, directly retrieves and returns the cached value.

4. **Implementation Example**:
   - Create a `cache` (e.g., an object in JavaScript).
   - Check if the input parameter exists in the cache:
     - If it exists: Return the cached value.
     - If it doesn’t: Compute the result, store it in the cache, and return it.

#### **Example Code Explanation**:
```javascript
let cache = {}; // Cache storage

function memorizedAddTo80(n) {
    if (n in cache) { // Check if the value is already cached
        return cache[n];
    } else {
        cache[n] = n + 80; // Compute and store the value in cache
        return cache[n];
    }
}

console.log(memorizedAddTo80(5)); // First call: Computes and caches the result
console.log(memorizedAddTo80(5)); // Second call: Reuses the cached result
```

- **First Call (Input: 5)**:
  - Calculates `5 + 80 = 85`.
  - Stores `85` in the cache (`cache[5] = 85`).
- **Second Call (Input: 5)**:
  - Retrieves `85` from the cache instead of recalculating.

#### **Benefits of Memorization**:
1. **Efficiency**: Speeds up programs by avoiding redundant calculations.
2. **Time Complexity**: For repeated inputs, fetching from a cache is **O(1)** (constant time).
3. **Dynamic Handling**: Automatically recalculates for new inputs and caches the results for future use.

#### **Memorization in Dynamic Programming**:
- Core technique used in DP to optimize recursive solutions by storing intermediate results.
- Example: Storing results of Fibonacci sequence calculations to avoid repeated recursive calls.

#### **Takeaway**:
Memorization leverages caching to optimize function calls, making programs more efficient. It’s particularly valuable in solving problems with overlapping subproblems, as seen in **dynamic programming**.
"""