"""
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

"""
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ws=0
        f={}
        for i in range(k):
            ws+=nums[i]
            if nums[i] in f:
                f[nums[i]]+=1
            else:
                f[nums[i]]=1
        m=0
        if len(f)==k:
            m=max(m,ws)
        for i in range(k,len(nums)):
            if len(f)==k:
                m=max(m,ws)
            ws+=nums[i]
            ws-=nums[i-k]
            if f[nums[i-k]]>1:
                f[nums[i-k]]-=1
            else:
                del f[nums[i-k]]
            if nums[i] in f:
                f[nums[i]]+=1
            else:
                f[nums[i]]=1
        if len(f)==k:
            m=max(m,ws)
        return m
obj=Solution()
res=obj.maximumSubarraySum([1,5,4,2,9,9,9],3)
print(res)
