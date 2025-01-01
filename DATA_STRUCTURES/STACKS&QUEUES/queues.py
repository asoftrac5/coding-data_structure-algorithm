"""
### Notes on Queues

1. **Definition**:  
   - A **queue** is a **linear data structure** that operates on a **FIFO (First In, First Out)** principle.  
   - Analogy: Like a line for a roller coaster—first person in line gets served first.

2. **Key Operations**:  
   - **Enqueue (Push)**: Add an item to the end of the queue.  
   - **Dequeue (Remove)**: Remove the item from the front of the queue.  
   - **Peek**: View the first item in the queue without removing it.  
   - **Lookup**: Rarely used due to inefficiency (**O(n)** complexity).

3. **Use Cases**:  
   - **Waitlist Applications**: E.g., concert ticket purchases or restaurant check-ins.  
   - **Ride-Share Services**: Requests are served in order of arrival.  
   - **Printer Queues**: Prints are processed in the order submitted.  
   - **Task Scheduling**: Jobs/tasks are executed in the order they are added.

4. **Complexity**:  
   - **Enqueue**: **O(1)** (constant time to add to the end).  
   - **Dequeue**: **O(1)** (constant time to remove from the front).  
   - **Peek**: **O(1)** (constant time to view the first item).  
   - **Lookup**: **O(n)** (inefficient due to sequential traversal).  

5. **Difference from Stacks**:  
   - **Queues**: FIFO—first item added is the first to be removed.  
   - **Stacks**: LIFO—last item added is the first to be removed.

6. **Why Not Use Arrays for Queues?**  
   - **Inefficiency**: Removing the first element (**unshift**) in an array requires shifting all subsequent elements, leading to **O(n)** complexity.  
   - **Better Options**: Use linked lists or other data structures optimized for **queue** operations.

7. **Real-World Examples**:  
   - **Ride-sharing apps**: Handling requests in order of arrival.  
   - **Printer services**: Managing print jobs from multiple sources.  
   - **Undo/Redo**: Can complement stacks for advanced undo/redo functionality.  

8. **Next Steps**:  
   - Implement a queue using code to understand its operations and limitations.  
   - Explore the differences in implementation using arrays and linked lists.
"""