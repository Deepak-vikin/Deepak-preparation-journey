"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first = -1
        last = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        last = left - 1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        first = right + 1
        if first <= last and first < len(nums) and nums[first] == target:
            return [first, last]
        return [-1, -1]
obj=Solution()
res=obj.searchRange([5,7,7,8,8,10], 8)
print(res)