"""
### **Important Notes: Depth-First Search (DFS)**

---

#### **Definition**
- DFS is a tree or graph traversal method where the search goes as deep as possible along one branch before backtracking and exploring other branches.
- It explores nodes in a "deep first" manner, starting at the root and diving into children before returning to siblings.

---

#### **How DFS Works**
1. **Start at the root node.**
2. Traverse the **leftmost branch** until a leaf node is reached.
3. **Backtrack** to the most recent ancestor with unexplored children.
4. Continue exploring until all nodes are visited.

---

#### **Example**
For a **binary search tree (BST)**:
```
       9
      / \
     4   20
    / \   / \
   1   6 15 170
```
DFS processes nodes in this order: **9, 4, 1, 6, 20, 15, 170**.

---

#### **Memory Requirements**
- DFS has **lower memory requirements** than BFS.
  - Only the current branch (path from root to the current node) is stored.
- Suitable for trees/graphs with fewer levels but many children.

---

#### **Applications**
- **Pathfinding in Mazes**: Mimics exploring all possible paths.
- **Game Trees**: Used in scenarios where depth exploration is needed.
- **Detecting Cycles** in graphs.

---

#### **Pros of DFS**
- **Lower Memory Usage**: Only tracks the current branch, unlike BFS, which tracks all children at a level.
- **Finds Solutions Quickly for Deep Targets**: If the target node is near the bottom of the tree, DFS may locate it faster.
- **Better for Deep Trees**: Efficient for problems with deep, narrow structures.

---

#### **Cons of DFS**
- **May Miss Optimal Path**: DFS does not guarantee the shortest path, as it prioritizes depth over breadth.
- **Risk of Infinite Loops**: In cyclic graphs, DFS can loop indefinitely without proper visited node tracking.
- **Unsuitable for Wide, Shallow Trees**: Traversal time increases with numerous shallow branches.

---

#### **Comparison with BFS**
| **Aspect**         | **DFS**                              | **BFS**                              |
|---------------------|--------------------------------------|--------------------------------------|
| **Order**           | Depth-first, exploring one branch    | Level-by-level, breadth-first        |
| **Memory Usage**    | Lower                                | Higher                               |
| **Shortest Path**   | Not guaranteed                      | Guaranteed in unweighted graphs      |
| **Performance**     | Better for deep, narrow structures  | Better for shallow, wide structures  |

---

#### **Next Steps**
- Explore **DFS Variations** and implement DFS in code.
- Compare DFS traversal orders and understand specific use cases.
"""