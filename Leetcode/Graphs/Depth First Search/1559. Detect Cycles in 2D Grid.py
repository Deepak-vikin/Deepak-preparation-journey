"""
Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.


Example 1:

Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:
"""
class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        n=len(grid)
        m=len(grid[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(x,y,parent):
            if x<0 or y<0 or x>=n or y>=m:
                return False
            visited.add((x,y))
            for sx,sy in directions:
                nx=sx+x
                ny=sy+y
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]==grid[x][y]:
                    if (nx,ny) not in visited:
                        if dfs(nx,ny,(x,y)):
                            return True
                    elif (nx,ny)!=parent:
                        return True
            return False
        global_visited=set([])
        for i in range(n):
            for j in range(m):
                if (i,j) in global_visited:
                    continue
                visited=set([])
                if dfs(i,j,-1):
                    return True
                global_visited.update(visited)
        return False
obj=Solution()
res=obj.containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]])
print(res)