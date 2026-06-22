"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.



Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        c=0
        m=0
        while i<len(nums):
            if nums[i]!=1:
                c=max(c,m)
                m=0
            else:
                m+=1
            i+=1
        c=max(c,m)
        return c
obj=Solution()
res=obj.findMaxConsecutiveOnes([1,0,1,0,1,0,1])
print(res)