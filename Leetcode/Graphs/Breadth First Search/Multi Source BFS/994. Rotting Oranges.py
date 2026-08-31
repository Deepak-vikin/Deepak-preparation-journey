"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        m=len(grid)
        n=len(grid[0])
        sx=sy=0
        found=0
        queue=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    found=1
                    sx,sy=i,j
                    queue.append((sx,sy,0))
        if fresh==0:
            return 0
        if not found:
            return -1

        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            if fresh==0:
                return time+1
            sx,sy,time=queue.popleft()
            for x,y in directions:
                nx=sx+x
                ny=sy+y
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                    grid[nx][ny]=2
                    fresh-=1
                    queue.append((nx,ny,time+1))
        return -1
obj=Solution()
res=obj.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print(res)



