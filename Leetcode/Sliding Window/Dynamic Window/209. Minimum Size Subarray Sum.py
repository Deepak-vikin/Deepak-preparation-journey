"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m=float("inf")
        left=0
        s=0
        for right in range(len(nums)):
            s+=nums[right]
            while s>=target:
                m=min(m,right-left+1)
                s-=nums[left]
                left+=1
        if m!=float("inf"):
            return m
        return 0
obj=Solution()
res=obj.minSubArrayLen(7,[2,3,1,2,4,3])
print(res)