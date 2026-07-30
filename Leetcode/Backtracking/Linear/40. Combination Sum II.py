"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def solve(i,s,path):
            if s==target:
                res.append(path)
                return
            if i>=len(candidates) or s>target:
                return
            solve(i+1,s+candidates[i],path+[candidates[i]])
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            solve(i+1,s,path)
            return
        solve(0,0,[])
        return res
obj=Solution()
res =obj.combinationSum2([2,3,6,7],7)
print(res)

