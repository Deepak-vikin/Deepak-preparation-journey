"""
You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).

The total value of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value divisible by k.



Example 1:


Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5

Output: 2

Explanation:

The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

Example 2:


Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3

Output: 6

Explanation:

The grid contains six islands, each with a total value that is divisible by 3.
"""


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y, ):
            nonlocal curr
            visited.add((x, y))
            curr += grid[x][y]
            for sx, sy in directions:
                nx = sx + x
                ny = sy + y
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and grid[nx][ny] != 0:
                    dfs(nx, ny)

        count = 0
        visited = set([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and (i, j) not in visited:
                    curr = 0
                    dfs(i, j)
                    print(curr)
                    if curr % k == 0:
                        count += 1
        return count
obj=Solution()
res=obj.countIslands([[3,0,3,0], [0,3,0,3], [3,0,3,0]],3)
print(res)