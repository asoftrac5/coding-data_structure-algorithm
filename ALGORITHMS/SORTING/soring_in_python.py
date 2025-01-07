"""
The default sorting algorithm used by Python's `sort()` method (for lists) and the `sorted()` function is **Timsort**.

---

### **What is Timsort?**
- **Origin:** Developed by Tim Peters in 2002 for Python.
- **Type:** Hybrid sorting algorithm.
- **Based on:** Combines the concepts of **Merge Sort** and **Insertion Sort**.

---

### **Key Features of Timsort:**
1. **Performance:**
   - **Best Case:** \( O(n) \) (if the data is already sorted or nearly sorted).
   - **Average Case:** \( O(n \log n) \).
   - **Worst Case:** \( O(n \log n) \).

2. **Stability:**
   - Timsort is a stable sorting algorithm, meaning it preserves the relative order of equal elements.

3. **Adaptive:**
   - Takes advantage of already sorted or partially sorted data (runs). This adaptation improves performance in real-world scenarios.

4. **Space Complexity:**
   - \( O(n) \) auxiliary space, mainly used for merging.

---

### **How Timsort Works:**
1. **Divide Input into Runs:**
   - Identifies small segments (called **runs**) that are already sorted or nearly sorted.
   - If runs are shorter than a certain size (usually 32), it sorts them using **Insertion Sort**.

2. **Merge Runs:**
   - Merges these sorted runs using a method similar to **Merge Sort**.
   - Carefully merges runs to optimize space and time.

---

### **Why Timsort is Used in Python:**
- It is highly efficient for real-world data due to its adaptive nature.
- It works well with datasets that are partially ordered, a common case in practical applications.
- Its stability makes it suitable for complex data types like tuples or objects. 

---

### **Fun Fact:**
Timsort is not exclusive to Python. It is also used in Java's `Arrays.sort()` method (for objects) and other programming environments due to its robust performance.
"""