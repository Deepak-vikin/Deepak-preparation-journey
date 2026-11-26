"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
"""
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[-1]*m for _ in range(n)]
        def solve(i,j):
            if i==0 and j==0:
                return grid[0][0]
            if dp[i][j]!=-1:
                return dp[i][j]
            if i==0:
                return grid[i][j]+solve(i,j-1)
            if j==0:
                return grid[i][j]+solve(i-1,j)
            take1=grid[i][j]+solve(i-1,j)
            take2=grid[i][j]+solve(i,j-1)
            dp[i][j]=min(take1,take2)
            return dp[i][j]
        return solve(n-1,m-1)
obj=Solution()
res=obj.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
print(res)