"""
### Important Notes on Depth-First Search (DFS)

1. **Definition**:
   - DFS explores the deepest nodes of a tree or graph first before backtracking and exploring other branches.

2. **Types of DFS Traversal**:
   - **In-Order**:
     - Traverses left subtree → root node → right subtree.
     - Useful for binary search trees (BSTs) because it returns nodes in sorted order.
     - Example: For a BST, the traversal order might be `1 → 4 → 6 → 9 → 15 → 20 → 170`.

   - **Pre-Order**:
     - Traverses root node → left subtree → right subtree.
     - Useful for recreating a tree structure.
     - Example: The traversal order might be `9 → 4 → 1 → 6 → 20 → 15 → 170`.

   - **Post-Order**:
     - Traverses left subtree → right subtree → root node.
     - Useful when deleting or processing child nodes before their parent.
     - Example: The traversal order might be `1 → 6 → 4 → 15 → 170 → 20 → 9`.

3. **Applications**:
   - **In-Order**:
     - Retrieving sorted elements from a binary search tree.
   - **Pre-Order**:
     - Reconstructing a tree.
   - **Post-Order**:
     - Evaluating expressions in an expression tree (child-first computation).

4. **Key Points**:
   - DFS can be implemented using recursion or a stack.
   - The traversal order depends on the application and the specific needs of the algorithm.
   - While the traversal orders may seem confusing initially, understanding their practical use cases clarifies their importance.

5. **Comparison with BFS**:
   - DFS explores deeper nodes first, while BFS explores nodes level by level.
   - DFS has lower memory consumption compared to BFS for wide trees.
   - Traversal order in DFS depends on the chosen method (in-order, pre-order, or post-order). 

6. **Next Steps**:
   - Practice implementing these traversal methods in code to solidify understanding.
   - Use different traversal methods depending on specific problem requirements.
"""