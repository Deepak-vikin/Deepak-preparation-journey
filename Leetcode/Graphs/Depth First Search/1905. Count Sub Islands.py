"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

Example 1:
Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
"""
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited=set([])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        n=len(grid2)
        m=len(grid2[0])
        def dfs(x,y):
            nonlocal flag
            if x<0 or y<0:
                return
            if grid1[x][y]==0:
                flag=False
                return
            visited.add((x,y))
            grid2[x][y]=5
            for sx,sy in directions:
                nx=sx+x
                ny=sy+y
                if 0<=nx<n and 0<=ny<m and grid2[nx][ny]==1 and (nx,ny) not in visited:
                    dfs(nx,ny)
        count=0
        for i in range(n):
            for j in range(m):
                if grid2[i][j]==1:
                    flag=True
                    dfs(i,j)
                    if flag:
                        count+=1
        return count