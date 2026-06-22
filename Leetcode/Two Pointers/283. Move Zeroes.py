"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0
        while i < len(nums) and j < len(nums):
            if nums[j] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j += 1
            else:
                j += 1
obj=Solution()
res=obj.moveZeroes([0,1,0,3,12])
print(res)