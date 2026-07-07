"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        f={0:1}
        pref=0
        count=0
        for i in range(len(nums)):
            pref+=nums[i]
            if pref-k in f:
                count+=f[pref-k]
            if pref in f:
                f[pref]+=1
            else:
                f[pref]=1
        return count
obj=Solution()
res=obj.subarraySum([1,1,1],2)
print(res)