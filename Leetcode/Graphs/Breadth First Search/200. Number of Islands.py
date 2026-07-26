"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        islands = 0
        visited = set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and (i, j) not in visited:
                    queue = deque([(i, j)])
                    visited.add((i, j))
                    islands += 1
                    while queue:
                        sx, sy = queue.popleft()
                        for x, y in directions:
                            nx = sx + x
                            ny = sy + y
                            if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == "1":
                                if (nx, ny) not in visited:
                                    visited.add((nx, ny))
                                    queue.append((nx, ny))
        return islands

obj=Solution()
res=obj.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(res)