"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.



Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        queue = deque([])
        visited = set()
        for i in range(n):
            if board[i][0] == "O":
                queue.append((i, 0))
                board[i][0] = "#"
            if board[i][m - 1] == "O":
                queue.append((i, m - 1))
                board[i][m - 1] = "#"
        for i in range(m):
            if board[0][i] == "O":
                queue.append((0, i))
                board[0][i] = "#"
            if board[n - 1][i] == "O":
                queue.append((n - 1, i))
                board[n - 1][i] = "#"
        directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        while queue:
            sx, sy = queue.popleft()
            for x, y in directions:
                nx = sx + x
                ny = sy + y
                if 0 <= nx < n and 0 < ny < m and board[nx][ny] == "O" and (nx, ny) not in visited:
                    board[nx][ny] = "#"
                    queue.append((nx, ny))
                    visited.add((nx, ny))
        for i in range(n):
            for j in range(m):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

obj=Solution()
res=obj.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
print(res)