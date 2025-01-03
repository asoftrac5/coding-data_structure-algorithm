"""
### Important Notes on Unbalanced Binary Search Trees (BSTs)

#### 1. **The Problem with Unbalanced BSTs**:
   - When inserting nodes in a specific order (e.g., increasing or decreasing values), the BST can become **unbalanced**.
   - Example:
     - Insert 86 → 90 → 99. All nodes are added to the right, forming a skewed tree.
   - **Effect**: 
     - The tree starts to resemble a **linked list**.
     - Operations (e.g., lookup, insert, delete) degrade from \( O(\log n) \) to **linear time** \( O(n) \).

#### 2. **Performance Impact**:
   - Balanced BSTs: Maintain \( O(\log n) \) time complexity for lookup, insert, and delete.
   - Unbalanced BSTs: Result in worst-case \( O(n) \) time complexity due to sequential traversal.

#### 3. **Key Takeaways**:
   - **Why are unbalanced BSTs bad?**
     - They lose the performance advantage of logarithmic time complexity.
     - Lookups and operations become slower, similar to traversing an unsorted list.

#### 4. **How to Balance a BST?**
   - Balancing algorithms ensure the height of the tree remains minimized:
     - **AVL Trees**: Automatically balance after insertions and deletions by rotating nodes.
     - **Red-Black Trees**: Maintain balance using color properties and rotations.
   - **Trade-offs**:
     - Complexity: Balancing introduces overhead but ensures consistent \( O(\log n) \) performance.

#### 5. **Relevance in Programming and Interviews**:
   - Many programming languages (e.g., Java, Python) have built-in balanced BST implementations.
   - **Interview Tip**:
     - You won’t usually be asked to implement balancing algorithms in interviews.
     - However, you should understand:
       - The concept of balancing.
       - Why unbalanced trees are inefficient.
       - The trade-offs of different balancing techniques.

#### 6. **Summary**:
   - **Balanced BSTs**:
     - Provide efficient operations with logarithmic time complexity.
     - Require additional algorithms to maintain balance (e.g., AVL, Red-Black Trees).
   - **Unbalanced BSTs**:
     - Degrade performance to linear time in worst cases.
   - **Next Steps**:
     - Learn the pros and cons of BSTs.
     - Build a simple BST to understand basic operations. 

### Recommendation:
   - Explore tools like **VisuAlgo** to visualize unbalanced vs. balanced trees.
   - Practice coding basic BST operations to solidify understanding.
"""