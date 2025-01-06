"""
### Important Notes on Selection Sort

1. **Introduction to Selection Sort**:
   - Selection sort is a **simple sorting algorithm** that is conceptually easy to understand.
   - It sorts a list by repeatedly finding the **smallest element** from the unsorted portion and placing it in the correct position.

2. **How Selection Sort Works**:
   - Starts with the first element as the **current smallest**.
   - Scans the list to find the smallest element in the unsorted portion.
   - Once the smallest element is identified, it is **swapped** with the element at the current position.
   - Repeats this process, moving to the next position, until the entire list is sorted.

3. **Algorithm Steps**:
   - Iterate through the list.
   - For each index \(i\):
     - Identify the smallest element from \(i\) to the end of the list.
     - Swap this smallest element with the element at index \(i\).
   - Continue this process until all elements are sorted.

4. **Efficiency of Selection Sort**:
   - **Time Complexity**:
     - **Best Case**: \(O(n^2)\) (even for a sorted list, it scans the entire unsorted portion for the smallest element).
     - **Average Case**: \(O(n^2)\).
     - **Worst Case**: \(O(n^2)\).
   - **Space Complexity**:
     - \(O(1)\) (in-place sorting; does not require extra memory for additional data structures).

5. **Comparison to Bubble Sort**:
   - Like bubble sort, selection sort has \(O(n^2)\) time complexity and is not suitable for large datasets.
   - Selection sort reduces the number of swaps compared to bubble sort, as elements are only swapped when the smallest element is identified.

6. **Key Characteristics**:
   - Selection sort is a **comparison-based** algorithm.
   - It's more efficient than bubble sort in terms of the number of swaps but still inefficient for large datasets.
   - Commonly used as a learning tool rather than in practical applications.

7. **Challenge**:
   - Try implementing selection sort:
     - Use nested loops: an outer loop to iterate over the list and an inner loop to find the smallest element in the unsorted portion.
     - Swap the smallest element with the current element at each step.
   - Test your implementation on different datasets and compare your solution with the next lesson.
"""