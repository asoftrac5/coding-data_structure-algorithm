"""
### **Important Notes: Breadth-First Search (BFS)**

#### **Definition**
- BFS is a method for searching or traversing a tree or graph level by level.
- Starting at the **root node**, it processes all nodes at the current level before moving to the next level.

---

#### **How BFS Works**
1. Start at the **root node**.
2. Visit all nodes at the **second level** (from left to right).
3. Move to the **third level**, processing nodes left to right.
4. Repeat this process level by level until:
   - The target node is found.
   - All nodes are visited.

---

#### **Example**
- For a **binary search tree (BST)** with nodes:
  ```
       9
      / \
     4   20
    / \   / \
   1   6 15 170
  ```
- BFS processes nodes in this order: **9, 4, 20, 1, 6, 15, 170**.

---

#### **Memory Requirements**
- BFS uses **additional memory** to track all nodes and their children on a given level.
  - Requires storing nodes in a **queue**.
  - Memory usage increases with the breadth of the tree (wider trees require more memory).

---

#### **Applications**
- **Shortest Path**: Useful for finding the shortest path in an unweighted graph.
- **Level-Wise Operations**: Ideal for scenarios requiring level-wise processing.

---

#### **Pros of BFS**
- **Complete Search**: Ensures all nodes at one level are processed before moving deeper.
- **Optimal for Shortest Path**: Finds the shortest path in terms of the number of edges in unweighted graphs.

---

#### **Cons of BFS**
- **Memory Intensive**: Stores many nodes simultaneously, especially in wide trees/graphs.
- **Not Suitable for Deep Trees**: Memory usage grows with the tree's breadth, making it inefficient for extremely wide structures.

---

#### **Comparison to DFS**
- BFS processes nodes level by level, whereas DFS explores deeper nodes first.
- BFS uses more memory compared to DFS, but it guarantees the shortest path in unweighted graphs.

--- 

#### **Next Steps**
- Explore **Depth-First Search (DFS)** for a comparison in approach and efficiency.
"""