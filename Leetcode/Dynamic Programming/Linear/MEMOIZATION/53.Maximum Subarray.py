"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        dp[0]=nums[0]
        def func(num):
            if num<0:
                return 0
            if dp[num]!=-1:
                return dp[num]
            dp[num]=max(nums[num],nums[num]+func(num-1))
            return dp[num]
        func(n-1)
        return max(dp)
obj=Solution()
res=obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)