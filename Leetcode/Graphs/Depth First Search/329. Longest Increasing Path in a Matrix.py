"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).



Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        ans=0
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        dp=[[0]*m for _ in range(n)]
        def dfs(x,y):
            if dp[x][y]!=0:
                return dp[x][y]
            curr=1
            for sx,sy in directions:
                nx=sx+x
                ny=sy+y
                if 0<=nx<n and 0<=ny<m and matrix[nx][ny]>matrix[x][y]:
                    curr=max(curr,1+dfs(nx,ny))
            dp[x][y]=curr
            return curr
        ans=0
        for i in range(n):
            for j in range(m):
                ans=max(ans,dfs(i,j))
        return ans
obj=Solution()
res=obj.longestIncreasingPath([[1,1,1],[1,1,0],[1,0,1]])
print(res)