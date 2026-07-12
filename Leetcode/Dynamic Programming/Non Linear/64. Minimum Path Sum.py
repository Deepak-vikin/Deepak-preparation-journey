"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
from typing import List
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dp=[[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                else:
                    if i==0 and j!=0:
                        dp[i][j]=grid[i][j]+dp[i][j-1]
                    elif j==0 and i!=0:
                        dp[i][j]=grid[i][j]+dp[i-1][j]
                    else:
                        dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
        return dp[rows-1][cols-1]
obj=Solution()
res=obj.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
print(res)
