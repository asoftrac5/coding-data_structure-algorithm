# 1 - Sort 10 schools around your house by distance: 
# Sorting algorithm: Insertion Sort

# 2 - eBay sorts listings by the current bid amount
# Sorting algorithm: Radix Sort, Counting Sort

# 3 - Sort scores on ESPN
# Sorting algorithm: Quick Sort

# 4 - Massive database (can't fil all into memory) needs to sort through past year's user data
# Sorting algorithm: Merge Sort

# 5 - Almost sorted Udemy review data needs to update and add 2 new devices
# Sorting algorithm: Insertion Sort

# 6 - Temperature records for the past 50 years in Canada
# Sorting algorithm:    Radix or counting sort: 
#                       Quick Sort

# 7 - Large user name database needs to be sorted. Data is very random
# Sorting algorithm: Merge Sort or Quick Sort

# 8 - You want to teach sorting for the first time
# Sorting algorithm: Bubble sort, Selection Sort

"""
### **Important Notes on Choosing Sorting Algorithms for Different Scenarios**

#### **General Guidelines**
1. **Understand the problem:**  
   - Assess the size of the input, the nature of the data, and memory constraints.
   - Tailor your choice of sorting algorithm based on these factors.
2. **Explain your reasoning:**  
   - During interviews, clearly articulate why a specific algorithm suits the given problem.

---

#### **Case-by-Case Recommendations**

1. **Sorting 10 Schools by Distance:**
   - **Input Size:** Small (10 elements).  
   - **Algorithm:** **Insertion Sort**  
     - Simple to implement.
     - Efficient for small and nearly sorted data.
     - Space complexity: \( O(1) \).

---

2. **eBay Listings Sorted by Current Bid Amount:**
   - **Input Type:** Fixed-length integers within a small range.  
   - **Algorithm:** **Radix Sort** or **Counting Sort**  
     - Suitable for numbers in a specific range (e.g., $1–$100).  
     - Can outperform \( O(n \log n) \) algorithms for this type of data.  

---

3. **Sports Scores on ESPN:**
   - **Input Type:** Large and varied scores (includes decimals).  
   - **Algorithm:** **QuickSort**  
     - Efficient average-case performance: \( O(n \log n) \).  
     - Space complexity is better than Merge Sort.  

---

4. **Massive Database Sorted Externally (e.g., by Date):**
   - **Input Type:** Extremely large, cannot fit into memory.  
   - **Algorithm:** **Merge Sort**  
     - Guarantees \( O(n \log n) \) performance.  
     - Suitable for external sorting, where memory constraints are critical.

---

5. **Almost Sorted Udemy Review Data (Adding 2 New Reviews):**
   - **Input Type:** Mostly sorted data with small updates.  
   - **Algorithm:** **Insertion Sort**  
     - Best suited for small additions to a nearly sorted dataset.  
     - Efficient with minimal overhead.

---

6. **Temperature Records for the Past 50 Years in Canada:**
   - **Input Type:** Numbers within a range, possibly with decimals.  
   - **Algorithm Choices:**  
     - **Radix/Counting Sort:** If no decimals and range is small (e.g., -32°C to 40°C).  
     - **QuickSort:** For decimal-based temperatures (not supported by Radix/Counting Sort).  

---

7. **Large Username Database (Random and Unstructured):**
   - **Input Type:** Large and random.  
   - **Algorithm Choices:**  
     - **Merge Sort:** If memory availability is not a concern.  
     - **QuickSort:** If memory efficiency is important.  

---

8. **Teaching Sorting for the First Time:**
   - **Algorithm:** **Bubble Sort** or **Selection Sort**  
     - Simple to understand, making them ideal for educational purposes.  
     - Inefficient for real-world applications.  

---

#### **Key Takeaways**
- **Insertion Sort:** Best for small or nearly sorted datasets.
- **Radix/Counting Sort:** Ideal for numeric data in a fixed range.
- **QuickSort:** Common choice for general-purpose sorting with good average-case performance.
- **Merge Sort:** Reliable for large datasets or external sorting where memory usage is less critical.
- **Bubble/Selection Sort:** Primarily for teaching sorting concepts, not practical for real-world use.  

---

#### **Advice for Interviews**
- Match the algorithm to the problem's constraints.
- Justify your choice by considering factors like input size, type, memory requirements, and performance trade-offs.
- Show flexibility by discussing alternative approaches when appropriate.
"""
