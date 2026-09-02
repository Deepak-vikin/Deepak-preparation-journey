"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.



Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
"""


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        queue = deque([])
        visited = set([])
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1:
                    if grid[i][j] == 1:
                        queue.append((i, j))
                        grid[i][j] = 0
                        visited.add((i, j))
                if j == 0 or j == m - 1:
                    if grid[i][j] == 1:
                        queue.append((i, j))
                        grid[i][j] = 0
                        visited.add((i, j))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            sx, sy = queue.popleft()
            for x, y in directions:
                nx = sx + x
                ny = sy + y
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    queue.append((nx, ny))
                    visited.add((nx, ny))
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
        return count
obj=Solution()
res=obj.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
print(res)