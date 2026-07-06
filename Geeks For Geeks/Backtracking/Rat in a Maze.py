"""
Given a binary matrix maze[][] of size n × n containing values 0 and 1, find all possible paths for a rat to travel from the source cell (0, 0) to the destination cell (n - 1, n - 1). The rat can move in four directions: up(U), down(D), left(L), and right(R).

1 represents an open cell through which the rat can move.
0 represents a blocked cell that cannot be traversed.

The rat can move only through open cells and cannot visit the same cell more than once in a path. Return all valid paths as strings consisting of 'U', 'D', 'L', and 'R', representing the sequence of moves taken by the rat.

Note: Return the paths in lexicographically increasing order. If no valid path exists, return an empty list.

Examples:

Input: maze[][] = {{1, 0, 0, 0}, {1, 1, 0, 1}, {1, 1, 0, 0}, {0, 1, 1, 1}}
Output: ["DDRDRR", "DRDDRR"]
Explanation: There are two valid paths from the source cell (0, 0) to the destination cell (3, 3).
"""


class Solution:
    def ratInMaze(self, maze):
        solution = [[0 for _ in range(len(maze))] for _ in range(len(maze))]
        n = len(maze)
        res = []

        def findsoln(x, y, solution, st):
            nonlocal n, res
            if x < 0 or y < 0 or x >= n or y >= n or solution[x][y] == 1 or maze[x][y] == 0:
                return
            if x == n - 1 and y == n - 1:
                res.append(st)
                return
            solution[x][y] = 1
            findsoln(x + 1, y, solution, st + "D")
            findsoln(x, y - 1, solution, st + "L")
            findsoln(x - 1, y, solution, st + "U")
            findsoln(x, y + 1, solution, st + "R")
            solution[x][y] = 0
            return

        findsoln(0, 0, solution, "")
        res.sort()
        return res
obj=Solution()
res=obj.ratInMaze([[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]])
print(res)
