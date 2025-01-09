"""
### Important Notes on Depth-First Search (DFS) in Graphs

1. **Core Concept**:
   - DFS is like solving a maze: 
     - **Go as deep as possible** down one path.
     - **Backtrack** when hitting a dead end.
     - Continue exploring alternative paths until the desired node is found or all possibilities are exhausted.

2. **How DFS Works**:
   - Starts at a specified node (e.g., `0`).
   - Explores all child nodes along a path as deeply as possible before moving to the next branch.
   - Uses **recursion** or a **stack** for backtracking when a dead end is reached.
   - Suitable for both **directed** and **undirected** graphs.

3. **Key DFS Characteristics**:
   - **Purpose**:
     - Determines if a path exists between nodes.
     - Not designed for finding the shortest path.
   - **Advantages**:
     - **Low memory usage** compared to BFS because it doesn’t store all sibling nodes at each level.
   - **Limitations**:
     - Can become **slow** in very deep graphs due to:
       - Large number of recursive calls.
       - Increased **space complexity** from maintaining the call stack.

4. **Applications of DFS**:
   - **Maze-solving algorithms**: Mirrors the logic of exploring and backtracking in a physical maze.
   - **Path existence**: Checks if a node or path exists in a graph.
   - **Topological sorting**: Useful in directed acyclic graphs (DAGs) to determine task execution order.
   - **Connected components**: Identifies all connected components in a graph.

5. **Directed vs. Undirected Graphs**:
   - **Directed Graphs**: DFS respects the direction of edges (e.g., from `0` to `9`) and does not backtrack against the direction.
   - **Undirected Graphs**: DFS can move back and forth between connected nodes.

6. **Implementation Details**:
   - Uses recursion to break the problem into smaller subproblems.
   - Backtracking is inherent to DFS and mimics the stack-based nature of recursion.

7. **Comparison with BFS**:
   - **DFS Strengths**:
     - Efficient for exploring all paths or confirming path existence.
     - Uses less memory than BFS in sparse graphs.
   - **DFS Weaknesses**:
     - Can get stuck in deep or infinite loops without proper termination conditions.
     - Does not guarantee finding the shortest path.

8. **Space Complexity**:
   - Relies on the **call stack** during recursive execution.
   - If the graph is very deep, the stack can grow large, increasing memory usage.

By understanding DFS, you can implement algorithms for maze solving, pathfinding, and exploring connected components efficiently, particularly in scenarios where memory optimization is crucial or shortest paths are not required.
"""