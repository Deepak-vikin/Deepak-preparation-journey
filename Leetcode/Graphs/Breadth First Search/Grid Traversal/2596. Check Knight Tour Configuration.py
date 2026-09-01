"""
There is a knight on an n x n chessboard. In a valid configuration, the knight starts at the top-left cell of the board and visits every cell on the board exactly once.

You are given an n x n integer matrix grid consisting of distinct integers from the range [0, n * n - 1] where grid[row][col] indicates that the cell (row, col) is the grid[row][col]th cell that the knight visited. The moves are 0-indexed.

Return true if grid represents a valid configuration of the knight's movements or false otherwise.

Note that a valid knight move consists of moving two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The figure below illustrates all the possible eight moves of a knight from some cell.

Example 1:

Input: grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
Output: true
Explanation: The above diagram represents the grid. It can be shown that it is a valid configuration.
"""
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        queue=deque([(0,0)])
        directions=[(1,2),(2,1),(-1,2),(2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1)]
        visited=set([(0,0)])
        count=0
        while queue:
            sx,sy=queue.popleft()
            if count==(n*n)-1:
                return True
            for x,y in directions:
                nx=sx+x
                ny=sy+y
                if 0<=nx<n and 0<=ny<n and (nx,ny) not in visited and grid[nx][ny]==count+1:
                    visited.add((nx,ny))
                    queue.append((nx,ny))
                    count+=1
        return False
obj=Solution()
res=obj.checkValidGrid([[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]])
print(res)
