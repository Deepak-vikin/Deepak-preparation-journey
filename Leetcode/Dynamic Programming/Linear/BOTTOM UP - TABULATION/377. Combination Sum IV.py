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
Example 2:

Input: nums = [9], target = 3
Output: 0
"""
class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp=[0]*(target+1)
        dp[target]=1
        for s in range(target-1,-1,-1):
            for num in nums:
                if s+num<=target:
                    dp[s]+=dp[s+num]
        return dp[0]
obj=Solution()
res=obj.combinationSum4([2,3,4,5],6)
print(res)
