"""
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.



Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
"""

class Solution:
    def check(self, nums: List[int]) -> bool:
        s=sorted(nums)
        m=sorted(nums)
        n=len(nums)
        for i in range(n):
            r1=s[i:]+s[:i]
            r2=m[:i] + m[i:]
            if r1==nums or r2==nums:
                return True
        return False
obj=Solution()
res=obj.check([3,4,5,1,2])
print(res)