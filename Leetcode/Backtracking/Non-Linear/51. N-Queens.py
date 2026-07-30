"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        maze = [["."] * n for _ in range(n)]
        res = []
        cols = set()
        diag1 = set()
        diag2 = set()

        def solve(row):
            if row == n:
                res.append(["".join(r) for r in maze])
                return False
            for col in range(n):
                if (col in cols) or (row - col in diag1) or (row + col in diag2):
                    continue
                maze[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                solve(row + 1)
                maze[row][col] = "."
                diag1.remove(row - col)
                diag2.remove(row + col)
                cols.remove(col)

        solve(0)
        return res
obj=Solution()
res=obj.solveNQueens(4)
print(res)