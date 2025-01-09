"""
### Important Notes on Shortest Path Algorithms in Graphs

1. **Graph Traversal Context**:
   - BFS and DFS are sufficient for **unweighted graphs** but not for weighted graphs where edge weights matter.
   - Real-life examples like Google Maps require considering weights such as distances or traffic.

2. **Weighted Graphs**:
   - A **weighted graph** assigns numerical values (weights) to edges, representing factors like distance, cost, or time.
   - **Edge**: Connection between two nodes (vertices).
   - BFS and DFS do not account for weights, necessitating specialized algorithms.

3. **Specialized Algorithms**:
   - **Bellman-Ford Algorithm**:
     - Can handle **negative weights** in the graph.
     - Effective but computationally expensive with a time complexity of **O(V × E)** (quadratic).
     - Use Bellman-Ford for graphs that might have negative edge weights.
   - **Dijkstra's Algorithm**:
     - Faster and more efficient than Bellman-Ford for graphs **without negative weights**.
     - Time complexity depends on the implementation:
       - **O(V²)** for simple implementations.
       - **O((V + E) log V)** with priority queues (e.g., using a min-heap).
     - Ideal for most real-life weighted graphs with only non-negative weights.

4. **Comparison**:
   - **Bellman-Ford**:
     - Pros: Handles negative weights.
     - Cons: Slower, higher computational cost.
   - **Dijkstra’s**:
     - Pros: Faster and more efficient for non-negative weights.
     - Cons: Cannot handle negative weights.

5. **Real-World Use Cases**:
   - **Google Maps**: Find the fastest or shortest route based on road distance and traffic conditions.
   - **Recommendation Engines**: Identify optimal recommendations based on a weighted relationship graph.
   - **Network Routing**: Optimize data packet delivery paths in computer networks.

6. **Interview Considerations**:
   - In interviews, you are typically **not required to implement these algorithms** due to their complexity.
   - You should know:
     - When to use BFS vs. Bellman-Ford vs. Dijkstra’s algorithm.
     - Bellman-Ford is for graphs with negative weights.
     - Dijkstra’s is for weighted graphs without negative weights.

7. **Example Scenario**:
   - Given a weighted graph without negative weights and a task to find the shortest path:
     - Use **Dijkstra’s Algorithm**.
   - If the graph includes negative weights:
     - Use **Bellman-Ford Algorithm**.

8. **Fun Fact**:
   - **Richard Bellman** (Bellman-Ford algorithm) is also known for dynamic programming, a key concept in optimization.

### Summary
For weighted graphs:
- Use **Dijkstra’s Algorithm** for non-negative weights.
- Use **Bellman-Ford Algorithm** for negative weights.
Understanding the strengths and limitations of these algorithms is critical for solving shortest path problems efficiently in interviews and real-world applications.
"""