"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
from typing import List
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def solve(i,path):
            if i==len(nums):
                res.append(path)
                return
            if i>=len(nums):
                return
            solve(i+1,path+[nums[i]])
            solve(i+1,path)
        solve(0,[])
        res.sort()
        return res
obj=Solution()
res=obj.subsets([1,2,2])
print(res)
