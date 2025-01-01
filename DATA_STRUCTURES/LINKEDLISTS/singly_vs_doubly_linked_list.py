"""
### Notes on When to Use Singly vs. Doubly Linked Lists

#### **Singly Linked List**  

1. **Advantages**:  
   - **Simplicity**:  
     - Easier to implement compared to doubly linked lists.  
   - **Lower Memory Usage**:  
     - Requires less memory since it only stores a pointer to the next node.  
   - **Efficiency in Modifications**:  
     - Insertions and deletions are faster due to fewer pointer updates.  
     - Ideal for operations at the beginning of the list.  

2. **Disadvantages**:  
   - **One-Way Traversal**:  
     - Cannot traverse the list backward.  
   - **Loss of Head Node**:  
     - Losing the reference to the head node can result in the entire list being lost.  

3. **Best Use Cases**:  
   - Situations with limited memory or when memory usage is a priority.  
   - Scenarios where the focus is on fast insertions and deletions rather than searching.  
   - Suitable when operations are mostly at the start of the list.  

---

#### **Doubly Linked List**  

1. **Advantages**:  
   - **Bidirectional Traversal**:  
     - Can traverse both forward and backward.  
   - **Efficient Deletions**:  
     - Can delete a node without needing to traverse from the head to find the previous node.  

2. **Disadvantages**:  
   - **Complexity**:  
     - More complex to implement due to additional pointer management.  
   - **Higher Memory Usage**:  
     - Requires extra memory for the additional pointer to the previous node.  
   - **Slower Modifications**:  
     - Insertions and deletions involve updating both `next` and `previous` pointers, increasing operation overhead.  

3. **Best Use Cases**:  
   - When memory usage is not a primary concern.  
   - Scenarios requiring frequent backward traversal or complex operations like deleting a node without accessing the head.  
   - Useful when searching involves traversing both directions for optimization.  

---

#### **Key Interview Insights**  
- Singly linked lists are more commonly tested in technical interviews.  
- Be prepared for theoretical questions comparing singly and doubly linked lists, but practical problems often involve singly linked lists.  


"""