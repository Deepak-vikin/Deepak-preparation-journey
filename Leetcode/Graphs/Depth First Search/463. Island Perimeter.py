"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        perm=0
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        visited=set([])
        def dfs(x,y):
            nonlocal perm
            if x<0 or y<0 or (x,y) in visited:
                return
            visited.add((x,y))
            for sx,sy in directions:
                nx=sx+x
                ny=sy+y
                if nx<0 or nx>=n or ny<0 or ny>=m or grid[nx][ny]==0:
                    perm+=1
                else:
                    dfs(nx,ny)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visited:
                    dfs(i,j)
        return perm
obj=Solution()
res=obj.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
print(res)





