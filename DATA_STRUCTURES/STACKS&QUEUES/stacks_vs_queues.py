"""
### Notes on Stacks and Queues Exercise

1. **Purpose**:  
   - To understand how stacks and queues can be implemented using **arrays** or **linked lists**.

---

### **Stacks**
2. **Definition and Example**:  
   - Stacks operate on a **LIFO (Last In, First Out)** principle.  
   - Example: **Browser History**  
     - Google → Udemy → YouTube → Twitter.  
     - To navigate back:
       - Remove Twitter → Back to YouTube → Back to Udemy → Back to Google.

3. **Implementation Options**:  
   - Stacks can be implemented using **arrays** or **linked lists**.

4. **Key Question**:  
   - **Why choose arrays over linked lists for stacks, or vice versa?**

5. **Considerations**:  
   - **Arrays**:
     - Direct indexing provides quick access to elements.
     - Suitable for fixed-size stacks.
     - Potential overhead when resizing (e.g., dynamic allocation).  
   - **Linked Lists**:
     - Dynamic size, no need for resizing.
     - Can have slight overhead due to pointer management.

---

### **Queues**
6. **Definition and Example**:  
   - Queues operate on a **FIFO (First In, First Out)** principle.  
   - Example: **Waitlist App**  
     - Order of arrival: Matt → Joy → Samir → Pavel.  
     - Order of service: Matt (first) → Joy → Samir → Pavel (last).

7. **Implementation Options**:  
   - Queues can also be implemented using **arrays** or **linked lists**.

8. **Key Question**:  
   - **Which is better for queues: arrays or linked lists, or are they equal?**

9. **Considerations**:  
   - **Arrays**:
     - Removing the first element (**unshift**) requires shifting all subsequent elements, making it inefficient (**O(n)**).  
   - **Linked Lists**:
     - Removing the first node is more efficient (**O(1)**), as no shifting is needed.

---

### **Takeaways**
10. **Reflection**:  
    - Evaluate the trade-offs between arrays and linked lists for implementing **stacks** and **queues**.  
    - Consider **efficiency** (time complexity) and **memory usage** for each use case.

11. **Next Step**:  
    - Understand the implementation details for both data structures and their practical applications.  
    - Review the upcoming explanation to solidify these concepts.
"""