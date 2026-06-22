"""
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if abs(target-s)<abs(target-res):
                    res=s
                if s==target:
                    return target
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
        return res
obj=Solution()
res=obj.threeSumClosest([-1,0,1,2,-1,-4],2)
print(res)