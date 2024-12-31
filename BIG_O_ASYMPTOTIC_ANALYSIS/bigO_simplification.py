# We don't need to precisely calculate the bigO for each line

# Rule Book to Calculate the BigO

# Rule 1: Worst Case

"""
### **Notes on Big O and Worst-Case Analysis**

#### **Key Concepts**
1. **Big O Measures Worst-Case Scenario**:
   - When calculating Big O, always focus on the **worst-case scenario**.
   - Big O represents the scalability and efficiency of an algorithm under the most demanding conditions.

2. **Finding Nemo Example**:
   - **Scenario**: Searching for "Nemo" in an array of 10 elements.
   - Without optimization, the loop runs through all 10 elements even if "Nemo" is found earlier.
   - **Observation**: This behavior is wasteful and inefficient.

3. **Improving Efficiency with a `break` Statement**:
   - Use the `break` statement (or similar constructs in other languages) to exit the loop once the target is found.
   - Result: The loop stops as soon as "Nemo" is located, saving unnecessary iterations.

4. **Big O Focuses Only on Worst Case**:
   - Despite the `break` statement improving efficiency, **Big O complexity** doesn't change.
   - **Best Case**: If "Nemo" is the first element, the loop runs once.
   - **Worst Case**: If "Nemo" is the last element, the loop runs through all 10 elements.
   - **Big O Conclusion**: The complexity is still **O(n)** (linear time), as worst-case defines the upper limit.

5. **Scalability and Input Uncertainty**:
   - When analyzing algorithms, we assume the worst-case scenario since inputs are unpredictable.
   - Big O analysis ensures the algorithm performs acceptably regardless of the input.

---

#### **Takeaways**:
- Big O **does not account for optimizations** like `break` for best-case scenarios.
- Always evaluate **worst-case scenarios** to understand an algorithm's scalability.
- The **first rule of Big O**: Worst-case matters most in algorithm analysis.

"""

# Rule 2: Remove Constants

import math


def printFirstItemThenFirstHalfThenSayHi100Times(items):
    print(items[0])

    middleIndex = len(items) // 2
    index = 0

    while (index < middleIndex):
        print(items[index])
        index += 1
    
    for i in range(100):
        print("Hi")

# BigO calculations: O(1 + n/2 + 100) = O(n)

"""
### **Notes on Big O and Rule #2: Remove Constants**

---

#### **Key Concepts**

1. **Drop Constants in Big O**:
   - When analyzing Big O, **ignore constants** because they become insignificant as the input size grows larger.
   - Constants, such as dividing by 2 or adding a fixed number of steps, have negligible effects on the algorithm's scalability.

---

#### **Example 1: Print Items and Say Hi 100 Times**
- **Function Details**:
  - Logs the first item of an array → **O(1)**.
  - Logs the first half of the array → **O(n/2)**.
  - Logs "hi" 100 times → **O(100)**.

- **Initial Big O Calculation**:
  - `O(1 + n/2 + 100)`.

- **Apply Rule #2** (Drop Constants):
  - Ignore constants like `/2` and `+100` since they don't matter for large inputs.
  - Final Big O: **O(n)**.

---

#### **Why Drop Constants?**
- As input size (`n`) increases:
  - Dividing by 2 (`n/2`) becomes less significant compared to `n`.
  - Fixed steps like 100 iterations are negligible.
- Big O focuses on how the function scales, not on small details.

---

#### **Example 2: Compress Boxes Twice**
- **Function Details**:
  - Two separate loops, each iterating over the input array → **O(n) + O(n)**.

- **Initial Big O Calculation**:
  - `O(2n)`.

- **Apply Rule #2** (Drop Constants):
  - Ignore the multiplier `2` since it doesn't affect the growth rate.
  - Final Big O: **O(n)**.

---

#### **Graphs and Steepness**:
- Big O only cares about the **rate of growth**, not the steepness of the line.
- Even if an algorithm requires more operations (e.g., `O(2n)` vs. `O(n)`), both scale **linearly**, so the Big O is the same: **O(n)**.

---

#### **Big O Notations and Numbers**:
- You rarely see numbers in Big O notation unless:
  - Specific cases like **O(2^n)** (exponential growth) or **O(n²)** (quadratic growth).
  - The focus is usually on scalability patterns, not fixed values.

---

#### **Takeaways**:
1. **Drop Constants**:
   - Ignore multipliers or additions in Big O calculations for simplicity.
   - E.g., `O(n/2 + 100)` simplifies to **O(n)**.

2. **Focus on Growth Patterns**:
   - Big O describes the trend of the algorithm as input grows, not specific operational counts.

3. **Linear Time Example**:
   - Even if an algorithm has multiple linear steps (e.g., `O(2n)`), it still simplifies to **O(n)** because both are linear.

---

#### **Summary**:
- Rule #2 simplifies Big O analysis by ignoring constants, making it easier to understand scalability.
- This approach highlights how an algorithm behaves for large inputs, prioritizing **growth rates** over exact operational details.

"""

# Rule 3: Different terms for inputs

def compressBoxesTwice(boxes, boxes2):
    for i in range(boxes):
        print(i)

    for j in range(boxes2):
        print(j)

# O(a + b)

"""
### **Notes on Big O and Rule #3: Different Terms for Inputs**

---

#### **Key Concepts**

1. **Different Inputs Matter**:
   - If a function operates on **two separate inputs**, their sizes must be treated independently in Big O notation.
   - This rule prevents mistakes when calculating the complexity of functions with multiple inputs.

---

#### **Example 1: Compress Boxes Twice**
- **Function Details**:
  - Two loops iterate over the same input (`boxes` array).
  - **Big O Analysis**:
    - First loop: **O(n)**.
    - Second loop: **O(n)**.
    - Combined: **O(2n)** → **O(n)** (after dropping constants).

---

#### **Example 2: Two Separate Inputs**
- **Function Details**:
  - First loop iterates over `boxes` (first input).
  - Second loop iterates over `boxes2` (second input).
  - These inputs are **independent**, meaning one could have a size of 100 while the other could have a size of 1.

- **Big O Analysis**:
  - First loop depends on the size of `boxes` → **O(a)**.
  - Second loop depends on the size of `boxes2` → **O(b)**.
  - Combined: **O(a + b)**.

---

#### **Key Differentiation**:
- When **inputs are different**:
  - **Separate terms** must be used for each input's size.
  - Example: **O(a + b)**, **O(n + m)**.
- When **inputs are the same**:
  - Constants are dropped, and loops are combined as one → **O(n)**.

---

#### **Common Mistake**:
- Assuming two loops with different inputs can be combined into one term.
  - Incorrect: **O(2n)**.
  - Correct: **O(a + b)** (if the inputs differ).

---

#### **Next Steps: Nested Loops**:
- If one loop is **nested** inside another, the complexity is multiplied rather than added.
- Nested loops are covered in the next topic.

---

#### **Takeaways**:
1. **Rule #3: Different Terms for Inputs**:
   - When a function operates on multiple inputs, consider each input separately in Big O analysis.
   - Example: Two independent loops result in **O(a + b)**, not **O(n)**.

2. **Combine Inputs Only When Appropriate**:
   - Combine terms only if the loops iterate over the **same input**.

3. **Big O Remains Additive**:
   - For independent inputs, add their complexities.
   - For nested loops, multiply their complexities (covered later).

---

Let me know if you'd like clarification or additional examples!333
"""

# Log all pairs of array
boxes = ['a', 'b', 'c', 'd', 'e']

def logAllPairsOfArray(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i], array[j])

logAllPairsOfArray(boxes)

# O(n * n) = O(n^2) - Quadratic Time


"""
### **Notes on Nested Loops and Big O (Quadratic Time)**

---

#### **Key Concepts**

1. **Logging All Pairs of an Array**:
   - The task involves generating all pairs of elements from an array.
   - Example:
     - For an array `[a, b, c, d, e]`, the pairs would be:  
       `(a, a), (a, b), (a, c), ..., (e, d), (e, e)`.

2. **Implementation**:
   - Use **nested loops** to iterate over the array:
     - Outer loop: Selects each element.
     - Inner loop: Iterates over all elements (including or excluding the outer loop’s current element).
   - Example (JavaScript):
     ```javascript
     function logAllPairs(array) {
         for (let i = 0; i < array.length; i++) {
             for (let j = 0; j < array.length; j++) {
                 console.log(array[i], array[j]);
             }
         }
     }
     ```

---

#### **Big O Analysis**

1. **Nested Loops**:
   - Outer loop runs **n** times (length of the array).
   - Inner loop runs **n** times for each iteration of the outer loop.
   - Total operations: **n × n = n²**.

2. **Big O**:
   - **O(n²)**: Known as **quadratic time complexity**.
   - This complexity occurs whenever loops are nested, leading to an exponential increase in operations.

3. **Quadratic Growth**:
   - As the input size increases, the number of operations grows exponentially.
   - Example:
     - For 2 elements: 4 operations (2²).
     - For 3 elements: 9 operations (3²).
     - For 10 elements: 100 operations (10²).

4. **Impact on Performance**:
   - Quadratic time is inefficient for large inputs due to rapid growth in operations.
   - This is why many interview questions focus on optimizing **O(n²)** solutions to something faster.

---

#### **General Rules for Nested Loops**

1. **Multiplication for Nested Loops**:
   - If loops are nested, their complexities are **multiplied**.
   - Example:
     - Outer loop: **O(a)**.
     - Inner loop: **O(b)**.
     - Total: **O(a × b)**.

2. **Addition for Sequential Loops**:
   - If loops are sequential (not nested), their complexities are **added**.
   - Example:
     - First loop: **O(a)**.
     - Second loop: **O(b)**.
     - Total: **O(a + b)**.

3. **Rule of Thumb**:
   - Operations at the **same indentation level** are **added**.
   - Nested operations are **multiplied**.

---

#### **Key Takeaways**

1. **Quadratic Time (O(n²))**:
   - Commonly occurs with nested loops.
   - Becomes inefficient as input size increases.

2. **Different Inputs**:
   - If nested loops iterate over **different inputs**, the complexity becomes **O(a × b)**.

3. **Optimization Focus**:
   - Many interview questions aim to reduce quadratic time complexity to linear or logarithmic time.

4. **Graph Representation**:
   - Quadratic complexity shows a **curved growth** on a graph, indicating rapid increases in operations as input size grows.

---

This understanding will help you analyze and optimize nested loops in algorithms effectively. Let me know if you need clarification or more examples!
"""

# Rule 4: Drop Non Dominants

def printAllNumbersThenPrintAllTheirSums(array):

    print("The numbers in the array are:")
    for i in range(len(array)):
        print(array[i])

    print("The sum of the numbers in the array are:")
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i] + array[j])

num = [1, 2, 3, 4, 5]
printAllNumbersThenPrintAllTheirSums(num)

# O(n + n^2)
# We skip O(n)

# Eg.: x = 5
# O(x^2 + 3x + 100 + x/2)
# Here, the constant 100 takes the lead but BigO considers the scalability.
# Eg.: x = 5000. In this case, x^2 takes lead with a huge difference.
# Therefore, O(n^2) - is the BigO for the program

"""
### **Notes on Big O and Rule #4: Drop Non-Dominant Terms**

---

#### **Key Concept: Drop Non-Dominant Terms**
- When calculating Big O, only consider the **most significant term** that dominates the algorithm’s growth as the input size increases.
- **Ignore smaller, less impactful terms** because their contribution becomes negligible for large inputs.

---

#### **Example 1: Print Numbers and All Pair Sums**
- **Function Details**:
  - First step: Log all numbers in the array → **O(n)**.
  - Second step: Log all pair sums using nested loops → **O(n²)**.

- **Initial Big O**:
  - **O(n + n²)**.

- **Apply Rule #4**:
  - Drop the non-dominant term (`O(n)`), as **O(n²)** grows much faster for large inputs.
  - **Final Big O**: **O(n²)**.

---

#### **Example 2: Complex Expression**
- **Expression**: \( O(x^2 + 3x + 1000 + \frac{x}{2}) \)
  - \( O(x^2) \): Dominant term (quadratic growth).
  - \( 3x \), \( 1000 \), \( \frac{x}{2} \): Non-dominant terms (linear or constant growth).

- **Simplification**:
  - Drop all non-dominant terms.
  - **Final Big O**: \( O(x^2) \).

- **Reasoning**:
  - For small \( x \), terms like \( 3x \) or \( 1000 \) might seem significant.
  - For large \( x \), \( x^2 \) (quadratic) dominates the growth, making other terms negligible.

---

#### **General Rules for Big O Simplification**
1. **Keep the Dominant Term**:
   - The term with the fastest growth as input increases is the dominant term.
   - Example: \( O(n^2 + n) \) simplifies to \( O(n^2) \).

2. **Drop Constants**:
   - Constants don’t impact the growth rate.
   - Example: \( O(2n^2) \) simplifies to \( O(n^2) \).

3. **Nested Loops**:
   - For each additional nested loop, the complexity increases exponentially.
   - Example: 3 nested loops result in \( O(n^3) \) (cubic complexity).

---

#### **Performance Impact**
- **Higher Powers are Worse**:
  - Quadratic (\( O(n^2) \)) is significantly worse than linear (\( O(n) \)).
  - Cubic (\( O(n^3) \)) or higher powers (\( O(n^4), O(n^5) \)) scale extremely poorly.

- **Optimization Focus**:
  - Many problems aim to reduce \( O(n^2) \) or \( O(n^3) \) complexity to something more efficient like \( O(n \log n) \) or \( O(n) \).

---

#### **Key Takeaways**
1. **Drop Non-Dominant Terms**:
   - Only retain the term with the fastest growth rate for simplicity.
   - Ignore constants and less significant terms.

2. **Dominant Term Example**:
   - \( O(x^2 + 3x + 1000) \) simplifies to \( O(x^2) \).

3. **Nested Loops**:
   - \( O(a \times b) \) for two loops with different inputs.
   - \( O(n^k) \) for \( k \) nested loops iterating over the same input.

4. **Avoid High Powers**:
   - Algorithms with \( O(n^3) \) or higher complexity scale poorly and are usually suboptimal.

---

#### **Important Note**:
- If an algorithm has three nested loops (\( O(n^3) \)), it is often inefficient and may need redesigning.
- Optimize nested loops wherever possible to reduce exponential growth.

---

With these rules, Big O calculations become more intuitive and simpler. Let me know if you'd like further clarifications or additional examples!
""" 