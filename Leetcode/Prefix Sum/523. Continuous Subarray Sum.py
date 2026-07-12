"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.


Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
from typing import List
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref=[]
        f={0:-1}
        pref.append(nums[0])
        for i in range(1,len(nums)):
            pref.append(pref[i-1]+nums[i])
        for i in range(len(pref)):
            if pref[i]%k not in f:
                f[pref[i]%k]=i
        for i in range(len(pref)):
            if pref[i]%k in f:
                if i-f[pref[i]%k]>=2:
                    return True
        return False
obj=Solution()
res=obj.checkSubarraySum([23,2,4,6,7],6)
print(res)
