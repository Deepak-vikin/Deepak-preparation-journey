"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
from typing import List
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        zero=0
        m=0
        while left<len(nums) and right<len(nums):
            if nums[right]==0:
                zero+=1
            while zero>k:
                if nums[left]==0:
                    zero-=1
                left+=1
            m=max(m,right-left+1)
            right+=1
        return m
obj=Solution()
print(obj.longestOnes([1,1,1,0,0,1,1,1,1,1], 3))
