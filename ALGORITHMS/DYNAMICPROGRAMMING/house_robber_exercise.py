"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

"""
# O(n) space solution
class Solution:
    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]

max_money = Solution()
print(max_money.rob([1, 2, 3, 1]))


# O(1) space solution

class Solution2:
    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        prev_rob = 0
        max_rob = 0
        for i in range(n):
            temp = max(max_rob, prev_rob + nums[i])
            prev_rob = max_rob
            max_rob = temp
        
        return max_rob


max_money2 = Solution2()
print(max_money2.rob([1, 2, 3, 1]))

nums = [2,7,9,3,1]
print(max_money2.rob(nums))