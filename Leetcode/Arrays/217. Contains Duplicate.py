"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]

Output: true

from typing import List
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in d:
            if d[i] > 1:
                return True
        return False
obj = Solution()
print(obj.containsDuplicate([1,2,3,1]))
