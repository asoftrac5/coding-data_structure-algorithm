"""
### Key Notes on When to Use Recursion

---

#### **When to Prefer Recursion**
1. **Tree or Graph Traversals**:
   - Recursion is ideal for **traversing** or **searching** through trees or graphs, such as:
     - Breadth-First Search (BFS).
     - Depth-First Search (DFS).

2. **Divide and Conquer Problems**:
   - Recursive solutions work well for problems that can be broken into smaller subproblems, such as:
     - **Sorting algorithms** (e.g., merge sort, quicksort).
     - Fibonacci sequence.
     - Factorial calculation.

3. **Tree-like Structures**:
   - Problems involving tree structures or converting data into trees often require recursion.

---

#### **Key Indicators of Recursive Problems in Interviews**
1. **Divisibility**:
   - The problem can be divided into **smaller subproblems** that are instances of the same problem.

2. **Identical Subproblems**:
   - Each subproblem involves **identical calculations**, only with smaller input sizes.

3. **Combining Results**:
   - The solution to the main problem can be achieved by combining solutions to the subproblems.

---

#### **Example of Divide and Conquer with Recursion**
- **Analogy**: Searching for a name in a phone book:
  1. You don’t start from the beginning.
  2. Instead, you split the problem into sections (e.g., A-M, N-Z).
  3. Repeat the process until the target name is found.
  - Recursive solutions mimic this divide-and-conquer approach.

---

#### **Challenges with Iterative Approaches**
1. **Tree Traversal**:
   - Iterative traversal requires managing a **stack** to keep track of nodes, adding complexity.
   - Recursive traversal is often more **straightforward**.

2. **Code Complexity**:
   - Iterative solutions can involve verbose and complicated code compared to recursion.

---

#### **Practice Suggestion**
1. **Tree Traversal Exercise**:
   - Write a **tree traversal function** (e.g., DFS or BFS) using recursion.
   - Then attempt the same task with loops to compare complexity.

2. **Algorithmic Challenges**:
   - Explore recursive solutions for problems like:
     - Fibonacci sequence.
     - Factorials.
     - Sorting algorithms.

---

#### **Summary of Rules for Recursive Problems**
- Problems that:
  1. Can be broken into smaller **subproblems**.
  2. Have **identical calculations** across subproblems.
  3. Require combining **leaf solutions** to solve the main problem.
- Use recursion when loops add unnecessary complexity, particularly for tree-like structures.
"""