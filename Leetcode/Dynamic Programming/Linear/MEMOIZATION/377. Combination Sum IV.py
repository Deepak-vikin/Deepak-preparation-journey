"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.



Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
"""
class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp={}
        n=len(nums)
        def solve(s):
            if s>target:
                return 0
            if s==target:
                return 1
            if s in dp:
                return dp[s]
            count=0
            for i in range(n):
                count+=solve(s+nums[i])
            dp[s]=count
            return count
        solve(0)
        return dp[0]
obj=Solution()
res=obj.combinationSum4([2,3,4,5],6)
print(res)