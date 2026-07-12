"""
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.


Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
from typing import List
"""
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.grid=grid
        self.m=len(grid)
        self.n=len(grid[0])
        self.solution=[[0]*self.n for _ in range(self.m)]
        mg=0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]!=0:
                    self.s=0
                    self.cm=0
                    self.findsoln(i,j,self.solution)
                    mg=max(self.cm,mg)
        return mg
    def findsoln(self,x,y,solution):
        if x<0 or y<0 or x>=self.m or y>=self.n or solution[x][y]==1 or self.grid[x][y]==0:
            return
        self.s+=self.grid[x][y]
        solution[x][y]=1
        self.findsoln(x+1,y,self.solution)
        self.findsoln(x-1,y,self.solution)
        self.findsoln(x,y+1,self.solution)
        self.findsoln(x,y-1,self.solution)
        self.cm=max(self.cm,self.s)
        self.s-=self.grid[x][y]
        solution[x][y]=0
        return

obj=Solution()
res=obj.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]])
print(res)
