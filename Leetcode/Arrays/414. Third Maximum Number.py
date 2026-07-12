"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.



Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

from typing import List
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l=sorted(set(nums))
        if len(l)>=3:
            return l[-3]
        else:
            return l[-1]
obj=Solution()
res=obj.thirdMax([1,2,3])
print(res)
