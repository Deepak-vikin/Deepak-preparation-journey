"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        n=len(grid)
        m=len(grid[0])
        solution=[[0]*m for _ in range(n)]
        def dfs(x,y,solution):
            if x<0 or y<0 or x>=n or y>=m or solution[x][y]==1 or grid[x][y]=="0":
                return
            solution[x][y]=1
            dfs(x+1,y,solution)
            dfs(x-1,y,solution)
            dfs(x,y+1,solution)
            dfs(x,y-1,solution)
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and solution[i][j]==0:
                    dfs(i,j,solution)
                    count+=1
        return count
obj=Solution()
res=obj.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
print(res)