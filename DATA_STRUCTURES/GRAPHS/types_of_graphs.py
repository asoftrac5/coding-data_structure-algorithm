"""
### Notes: Characteristics of Graphs  

1. **Types of Graphs**:
   - **Directed Graphs**:
     - Edges have a specific direction.
     - Example: 
       - **Twitter**: Followers and following relationships.
       - **One-way streets** in traffic systems.
   - **Undirected Graphs**:
     - Edges have no specific direction (bi-directional).
     - Example:
       - **Facebook**: Friend connections.
       - **Highways** between cities.

2. **Weighted vs. Unweighted Graphs**:
   - **Weighted Graphs**:
     - Edges have values (weights) associated with them.
     - Useful for optimization problems like:
       - **Google Maps**: Finding the shortest path.
       - **Travel planning**: Calculating the most efficient routes.
   - **Unweighted Graphs**:
     - Edges do not have weights.

3. **Cyclic vs. Acyclic Graphs**:
   - **Cyclic Graphs**:
     - Contain cycles where you can return to the starting node by traversing edges.
     - Common in weighted graphs like road networks.
   - **Acyclic Graphs**:
     - Do not contain cycles.
     - Example: Directed Acyclic Graphs (DAGs), often used in **dependency resolution** or **task scheduling**.

4. **Applications**:
   - Graphs are used to model systems like:
     - **Internet topology**: Nodes are IP addresses, edges are connections.
     - **Traffic flow**.
     - **Social networks**.

5. **Example**:
   - The **Optic Project**: A partial map of the Internet showing IP address connections as nodes and edges, is a powerful visualization of a graph.

6. **Summary**:
   - Understanding the characteristics of graphs (directed/undirected, weighted/unweighted, cyclic/acyclic) helps in selecting the appropriate graph type for real-world problems.
"""