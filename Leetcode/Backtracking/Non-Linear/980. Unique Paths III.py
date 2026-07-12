"""
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.



Example 1:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

from typing import List
"""
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.r=len(grid)
        self.c=len(grid[0])
        self.grid=grid
        self.solution=[[0]*self.c for _ in range(self.r)]
        self.count=0
        self.total=0
        sx=0
        sy=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    sx,sy=i,j
                if grid[i][j]!=-1:
                    self.total+=1
        step=1
        self.findsoln(sx,sy,self.solution,step)
        return self.count
    def findsoln(self,x,y,solution,step):
        if x<0 or y<0 or x>=self.r or y>=self.c or solution[x][y]==1 or self.grid[x][y]==-1:
            return False
        if self.grid[x][y]==2:
            if step==self.total:
                self.count+=1
            return False
        self.solution[x][y]=1
        if self.findsoln(x+1,y,solution,step+1):
            return True
        if self.findsoln(x-1,y,solution,step+1):
            return True
        if self.findsoln(x,y+1,solution,step+1):
            return True
        if self.findsoln(x,y-1,solution,step+1):
            return True
        self.solution[x][y]=0
        return False
obj=Solution()
res=obj.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
print(res)
