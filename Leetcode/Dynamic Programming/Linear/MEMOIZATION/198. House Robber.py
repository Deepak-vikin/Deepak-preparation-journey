"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        def func(num):
            if num==0:
                return nums[0]
            if num<0:
                return 0
            if dp[num]!=-1:
                return dp[num]
            sum1=func(num-2) + nums[num]
            sum2=func(num-1)
            dp[num]=max(sum1,sum2)
            return dp[num]
        return func(n-1)
obj=Solution()
res=obj.rob([1,2,3,1])
print(res)