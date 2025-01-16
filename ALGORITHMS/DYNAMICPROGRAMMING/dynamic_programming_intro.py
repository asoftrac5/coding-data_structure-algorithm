"""
### Important Notes on Dynamic Programming (DP)

#### **Overview**:
1. **Definition**:
   - **Dynamic Programming (DP)** is an **optimization technique**.
   - It solves problems by breaking them down into **smaller subproblems**, solving each once, and storing their solutions for reuse.

2. **Core Idea**:
   - Use **caching** (also called **memorization**) to store solutions to subproblems.
   - If the same subproblem arises again, reuse the stored solution instead of recomputing.

3. **Key Characteristics**:
   - Problems suitable for DP must exhibit:
     - **Overlapping Subproblems**: The same subproblems are solved multiple times.
     - **Optimal Substructure**: The solution to the overall problem can be composed of solutions to its subproblems.

4. **Applications**:
   - Widely used in algorithmic problem-solving and technical interviews.
   - Examples:
     - Fibonacci sequence.
     - Longest common subsequence.
     - Knapsack problem.
     - Pathfinding in grids (e.g., dynamic shortest paths).

5. **Dynamic Programming’s Name**:
   - The term itself is considered a **buzzword** with no specific meaning.
   - Its essence lies in optimization using caching, not in the literal meaning of the words "dynamic" or "programming."

6. **Importance**:
   - Crucial for efficient programming and algorithmic thinking.
   - Helps optimize solutions, especially for problems with repetitive computations.

#### **Next Steps**:
- Learn to identify problems where dynamic programming can be applied.
- Practice implementing caching techniques to optimize algorithms.
- Understand the difference between **top-down (memorization)** and **bottom-up (tabulation)** approaches.

#### **Takeaway**:
Dynamic programming isn't about "dynamics" or "programming"—it's about **solving problems smartly** by reusing solutions to subproblems through caching.
"""