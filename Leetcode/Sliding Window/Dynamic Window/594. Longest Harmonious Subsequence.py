"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.



Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation:

The longest harmonious subsequence is [3,2,2,2,3].

Example 2:

Input: nums = [1,2,3,4]

Output: 2

Explanation:

The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2
"""
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        nums.sort()
        left=0
        ans=0
        for right in range(len(nums)):
            diff=nums[right]-nums[left]
            while diff>1 and left<right:
                left+=1
                diff=nums[right]-nums[left]
            if diff==1:
                ans=max(ans,right-left+1)
        return ans
obj=Solution()
res=obj.findLHS([1,3,2,2,5,2,3,7])
print(res)
