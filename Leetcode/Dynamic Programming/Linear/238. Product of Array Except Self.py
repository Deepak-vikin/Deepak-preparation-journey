"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        dp1[0] = 1
        dp2[-1] = 1
        for i in range(1, len(nums)):
            dp1[i] = dp1[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            dp2[i] = dp2[i + 1] * nums[i + 1]
        res = []
        for i in range(len(nums)):
            res.append(dp1[i] * dp2[i])
        return res
obj=Solution()
res=obj.productExceptSelf([1,2,3,4])
print(res)