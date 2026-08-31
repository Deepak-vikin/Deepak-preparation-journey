"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.



Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        queue=deque([(0,0,1)])
        visited.add((0,0))
        directions=[(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
        if grid[0][0]==1:
            return -1
        if m-1==0 and n-1==0:
            return 1
        while queue:
            sx,sy,step=queue.popleft()
            for x,y in directions:
                nx=x+sx
                ny=y+sy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]==0 and (nx,ny) not in visited:
                    if nx==m-1 and ny==n-1:
                        return step+1
                    visited.add((nx,ny))
                    queue.append((nx,ny,step+1))
        return -1
obj=Solution()
res=obj.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])
print(res)
