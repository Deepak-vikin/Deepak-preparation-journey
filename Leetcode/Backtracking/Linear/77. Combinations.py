"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
from typing import List
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        arr=[]
        for i in range(1,n+1):
            arr.append(i)
        print(arr)
        def solve(i,path):
            if len(path)==k:
                res.append(path)
                return
            if i<0 or i>=len(arr):
                return
            solve(i+1,path+[arr[i]])
            solve(i+1,path)
        solve(0,[])
        return res
obj=Solution()
res=obj.combine(4,2)
print(res)
