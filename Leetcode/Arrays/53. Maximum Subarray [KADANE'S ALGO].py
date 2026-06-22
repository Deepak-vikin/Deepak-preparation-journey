"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=nums[0]
        cm=0
        for i in nums:
            cm+=i
            m=max(cm,m)
            if cm<0:
                cm=0
        return m
obj=Solution()
res=obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)