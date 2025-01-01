"""
### Notes on Doubly Linked Lists

1. **Definition**:  
   - A doubly linked list is a variation of a singly linked list where each node contains an extra pointer linking to the previous node.

2. **Structure**:  
   - Each node in a doubly linked list has:
     - A value.
     - A pointer to the next node.
     - A pointer to the previous node.

3. **Advantages**:  
   - **Bidirectional Traversal**:  
     - Unlike singly linked lists, doubly linked lists allow traversal in both forward and backward directions.
   - **Efficient Lookup**:  
     - Searching can start from either the head or tail, making lookup slightly faster for certain cases.
     - Theoretical time complexity remains \(O(n)\), but starting from the closer end can make searches more efficient in practice.

4. **Disadvantages**:  
   - **Increased Memory Usage**:  
     - Each node requires additional memory to store the pointer to the previous node.
   - **Complexity**:  
     - More pointers mean additional logic for managing insertions, deletions, and updates.

5. **Key Operations**:  
   - Adding a new node involves updating pointers for both the previous and next nodes.
   - Deleting or updating a node also requires managing both forward and backward pointers.

6. **Comparison with Singly Linked Lists**:  
   - **Traversal**:  
     - Singly linked lists can only traverse from head to tail.  
     - Doubly linked lists can traverse both ways.
   - **Memory Usage**:  
     - Doubly linked lists require more memory for the additional pointer.

7. **Optimization in Lookup**:  
   - In cases where the target element is in a known half of the list, traversal can start from the optimal end, reducing average search time.

8. **Practical Implementation**:  
   - A doubly linked list can be implemented by modifying a singly linked list to include an additional pointer for the previous node.

9. **Next Steps**:  
   - Convert the previously implemented singly linked list into a doubly linked list to understand its behavior and operations.
"""