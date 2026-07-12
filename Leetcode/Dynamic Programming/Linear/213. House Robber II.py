"""

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        dp=[0]*(len(nums))
        dp1=[0]*(len(nums))
        for i in range(len(nums)-1):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        for i in range(1,len(nums)):
            dp1[i]=max(dp1[i-1],nums[i]+dp1[i-2])
        print(dp)
        print(dp1)
        return max(dp1[-1],dp[-2])

obj=Solution()
res=obj.rob([2,3,2])
print(res)
