"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""

class Solution:
    def climbStairs(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]
    
ways_climb_stairs = Solution()
print(ways_climb_stairs.climbStairs(2))
print(ways_climb_stairs.climbStairs(3))

# Optimized solution
class Solution2:
    def climbStairs2(self, n):
        if n <= 3:
            return n
        
        prev1 = 3
        prev2 = 2
        cur = 0
        
        for _ in range(3, n):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur

        return cur
    
ways_to_climb_stairs_2 = Solution2()
print(ways_to_climb_stairs_2.climbStairs2(2))
print(ways_to_climb_stairs_2.climbStairs2(3))












"""
# With space complexity optimization
class Solution2:
    def climbStairs(self, n):
        if n <= 3:
            return n
        prev1 = 3
        prev2 = 2

        current_value = 0

        for i in range(3, n):
            current_value = prev1 + prev2
            prev2 = prev1
            prev1 = current_value

        return current_value
    
ways_to_climb_stairs = Solution2()
print(ways_to_climb_stairs.climbStairs(2))
print(ways_to_climb_stairs.climbStairs(3))
"""