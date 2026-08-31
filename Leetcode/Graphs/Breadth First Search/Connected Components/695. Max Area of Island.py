"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        marea=0
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(m):
            for j in range(n):
                area=0
                if grid[i][j]==1 and (i,j) not in visited:
                    area=1
                    queue=deque([(i,j)])
                    visited.add((i,j))
                    while queue:
                        sx,sy=queue.popleft()
                        for x,y in directions:
                            nx=sx+x
                            ny=sy+y
                            if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                                if (nx,ny) not in visited:
                                    visited.add((nx,ny))
                                    area+=1
                                    queue.append((nx,ny))
                marea=max(marea,area)
        return marea
obj=Solution()
res=obj.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
print(res)