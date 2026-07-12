"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
from typing import List
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def solve(i,path):
            if i==len(nums):
                res.append(path)
                return
            if i>=len(nums):
                return
            solve(i+1,path+[nums[i]])
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            solve(i+1,path)
            return
        solve(0,[])
        return res
obj=Solution()
res=obj.subsetsWithDup([1,2,2])
print(res)
