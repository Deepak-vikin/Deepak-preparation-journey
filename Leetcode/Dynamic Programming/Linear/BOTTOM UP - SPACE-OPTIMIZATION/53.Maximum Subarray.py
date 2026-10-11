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
        s=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            s=max(s+nums[i],nums[i])
            ans=max(s,ans)
        return ans
obj=Solution()
res=obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)