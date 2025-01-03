"""
### Important Notes on Heaps and Binary Heaps

#### 1. **What is a Heap?**
   - A **heap** is a tree-based data structure where:
     - **Max Heap**: The parent node has a value greater than or equal to its child nodes.
     - **Min Heap**: The parent node has a value less than or equal to its child nodes.
   - It is typically implemented as a **binary heap**, meaning each node can have at most two children.

#### 2. **Key Properties of Binary Heaps**:
   - **Structure**:
     - All levels are filled except possibly the last level, which is filled from left to right.
   - **Order**:
     - **Max Heap**: The value of each parent node is greater than its child nodes.
     - **Min Heap**: The value of each parent node is less than its child nodes.
   - The relationship between siblings (left and right children) is not significant, unlike binary search trees (BSTs).

#### 3. **Comparison to Other Data Structures**:
   - **Arrays**:
     - Arrays allow \( O(1) \) random access, but insertions and deletions (except at the end) require shifting, making them \( O(n) \).
   - **Linked Lists**:
     - Heaps have better ordering for priority-based operations compared to linked lists.
   - **Binary Search Trees (BSTs)**:
     - Heaps do not maintain the left < parent < right relationship as BSTs do, making lookup \( O(n) \) instead of \( O(\log n) \).

#### 4. **Time Complexity**:
   - **Insertion**: \( O(\log n) \)
     - New nodes are added at the leftmost available position and then **bubble up** to maintain heap order.
   - **Deletion**: \( O(\log n) \)
     - Removal usually involves replacing the root with the last node and **bubbling down** to restore heap order.
   - **Lookup**: \( O(n) \)
     - Finding a specific value involves checking all nodes as the heap is less ordered compared to a BST.

#### 5. **Why Use Binary Heaps?**
   - **Comparative Operations**:
     - Great for finding values that satisfy certain conditions (e.g., all values above a threshold).
   - **Efficient Priority Operations**:
     - Heaps are optimized for priority queues, where elements with the highest or lowest priority are retrieved efficiently.
   - **Use Cases**:
     - Data storage, priority queues, and certain sorting algorithms (e.g., **Heap Sort**).

#### 6. **Heap Operations Example**:
   - **Insertion**:
     - A new node is added at the leftmost available position and then bubbled up to maintain order.
   - **Example**: Inserting 100 into a max heap.
     - Add 100 at the leftmost available position.
     - Compare 100 with its parent nodes and swap if necessary until the heap property is restored.
   - **Deletion**:
     - The root (highest priority) is removed.
     - The last node replaces the root, and the tree is restructured by bubbling down.

#### 7. **Next Topic**:
   - Heaps are foundational to **priority queues**.
   - Understanding priority queues will help clarify why heaps are essential and how they differ from other tree structures.
"""