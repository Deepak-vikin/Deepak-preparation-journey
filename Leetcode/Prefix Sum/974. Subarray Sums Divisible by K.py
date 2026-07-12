"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
from typing import List
"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        f={0:1}
        pref=0
        count=0
        for i in range(len(nums)):
            pref+=nums[i]
            rem=pref%k
            if rem not in f:
                f[rem]=1
            else:
                count+=f[rem]
                f[rem]+=1
        return count
obj=Solution()
print(obj.subarraysDivByK([4,5,0,-2,-3,1]))
