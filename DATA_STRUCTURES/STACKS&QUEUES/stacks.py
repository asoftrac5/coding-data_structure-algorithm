"""
### Notes on Stacks

1. **Definition**:  
   - A stack is a **linear data structure** that operates on a **LIFO (Last In, First Out)** principle.
   - Visual analogy: Like a stack of plates where only the top plate is accessible.

2. **Key Operations**:  
   - **Push**: Add an item to the top of the stack.  
   - **Pop**: Remove the item from the top of the stack.  
   - **Peek**: View the item at the top without removing it.  
   - **Lookup**: Rarely used as it requires traversing the entire stack (**O(n)** complexity).

3. **Advantages and Use Cases**:  
   - **Last Value Access**: Useful when the last added value needs to be accessed first.  
   - **Function Calls**: Programming languages use stack architecture for function call management. Functions within functions follow LIFO to resolve calls.  
   - **Browser History**: Back and forward navigation use stacks to manage visited pages.  
   - **Undo/Redo**: Previous states in text editors or applications are stored in stacks for efficient undo/redo functionality.  
   - **Language Engines**: Stacks are integral to language-specific engines and can lead to issues like "Stack Overflow" when memory exceeds limits.  

4. **Complexity**:  
   - **Push**: **O(1)** (constant time to add to the top).  
   - **Pop**: **O(1)** (constant time to remove from the top).  
   - **Peek**: **O(1)** (constant time to view the top).  
   - **Lookup**: **O(n)** (traversing the stack is not efficient and rarely needed).

5. **Additional Insights**:  
   - **Stack Overflow**: Occurs when too many operations fill the stack memory, a common error in programming.  
   - **Practical Examples**: JavaScript engines and other runtime environments use stacks to manage function calls.

6. **Next Steps**:  
   - Implement a stack using code to understand its operations and behavior.  
   - Explore its relationship with queues and other data structures.  


"""