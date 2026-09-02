"""
You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

If isWater[i][j] == 0, cell (i, j) is a land cell.
If isWater[i][j] == 1, cell (i, j) is a water cell.
You must assign each cell a height in a way that follows these rules:

The height of each cell must be non-negative.
If the cell is a water cell, its height must be 0.
Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.
"""


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        solution = [[0] * n for _ in range(m)]
        queue = deque([])
        visited = set([])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] != 1:
                    solution[i][j] = float("inf")
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))
        while queue:
            sx, sy = queue.popleft()
            for x, y in directions:
                nx = sx + x
                ny = sy + y
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    new_dist = solution[sx][sy] + 1
                    if new_dist < solution[nx][ny]:
                        solution[nx][ny] = new_dist
                    queue.append((nx, ny))
                    visited.add((nx, ny))
        return solution
obj=Solution()
res=obj.highestPeak([[1,2,3],[4,5,6],[7,8,9]])
print(res)


