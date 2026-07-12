"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
from typing import List
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=[0]*len(nums)
        def perm(path):
            if len(path)==len(nums):
                res.append(path)
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                used[i]=1
                perm(path+[nums[i]])
                used[i]=0
        perm([])
        return res
obj=Solution()
