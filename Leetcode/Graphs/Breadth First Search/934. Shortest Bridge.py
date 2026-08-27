"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.



Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
"""


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        sx = sy = 0
        q = deque([])
        v = set([])
        found = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    visited = set([(i, j)])
                    queue = deque([(i, j)])
                    while queue:
                        sx, sy = queue.popleft()
                        for x, y in directions:
                            nx = sx + x
                            ny = sy + y
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and (nx, ny) not in visited:
                                queue.append((nx, ny))
                                visited.add((nx, ny))
                    found = 1
                    break
            if found:
                break
        for i, j in visited:
            grid[i][j] = 2
            q.append((i, j, 0))
            v.add((i, j))
        while q:
            sx, sy, dist = q.popleft()
            if grid[sx][sy] == 1:
                return dist - 1
            for x, y in directions:
                nx = sx + x
                ny = sy + y
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in v:
                    q.append((nx, ny, dist + 1))
                    v.add((nx, ny))
obj=Solution()
res=obj.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])
print(res)


