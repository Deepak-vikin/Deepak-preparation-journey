"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
from typing import List
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def findsoln(x,y,solution):
            nonlocal p
            if x<0 or y<0 or x>=row or y>=col or grid[x][y]==0:
                p+=1
                return False
            if solution[x][y]==1:
                return False
            solution[x][y]=1
            if findsoln(x+1,y,solution):
                return True
            if findsoln(x-1,y,solution):
                return True
            if findsoln(x,y+1,solution):
                return True
            if findsoln(x,y-1,solution):
                return True
            return False
        p=0
        row=len(grid)
        col=len(grid[0])
        solution=[[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    findsoln(i,j,solution)
                    return p
obj=Solution()
res=obj.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
print(res)
