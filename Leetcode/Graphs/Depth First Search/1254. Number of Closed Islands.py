"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
Return the number of closed islands.

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).
"""


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y):
            if x < 0 or y < 0 or x >= n or y >= m:
                return
            grid[x][y] = 1
            for sx, sy in directions:
                nx = sx + x
                ny = sy + y
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                    dfs(nx, ny)

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    if grid[i][j] == 0:
                        dfs(i, j)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1
        return count
obj=Solution()
res=obj.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]])
print(res)