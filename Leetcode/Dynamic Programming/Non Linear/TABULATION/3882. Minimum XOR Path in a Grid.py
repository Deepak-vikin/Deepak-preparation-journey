"""
You are given a 2D integer array grid of size m * n.

You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).

At each step, you may move either right or down.

The cost of a path is defined as the bitwise XOR of all the values in the cells along that path, including the start and end cells.

Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).



Example 1:

Input: grid = [[1,2],[3,4]]

Output: 6

Explanation:

There are two valid paths:

(0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
(0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6
The minimum XOR value among all valid paths is 6.

Example 2:

Input: grid = [[6,7],[5,8]]

Output: 9

Explanation:

There are two valid paths:

(0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
(0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11
The minimum XOR value among all valid paths is 9.

Example 3:

Input: grid = [[2,7,5]]

Output: 0

Explanation:

There is only one valid path:

(0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0
The XOR value of this path is 0, which is the minimum possible.
"""


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        """n=len(grid)
        m=len(grid[0])
        dp=[[0]*m for _ in range(n)]
        dp[0][0]=grid[0][0]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    continue
                if i==0:
                    dp[i][j]=grid[i][j]^dp[i][j-1]
                elif j==0:
                    dp[i][j]=grid[i][j]^dp[i-1][j]
                else:
                    dp[i][j]=min(grid[i][j]^dp[i-1][j],grid[i][j]^dp[i][j-1])
        return dp[-1][-1]

        a^b<c^b does not always make a<c .
        XOR is not monotonic.
        """
        n = len(grid)
        m = len(grid[0])
        dp = [[set([]) for _ in range(m)] for _ in range(n)]
        dp[0][0].add(grid[0][0])
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    for x in dp[i][j - 1]:
                        dp[i][j].add(x ^ grid[i][j])
                elif j == 0:
                    for x in dp[i - 1][j]:
                        dp[i][j].add(x ^ grid[i][j])
                else:
                    for x in dp[i - 1][j]:
                        dp[i][j].add(x ^ grid[i][j])
                    for x in dp[i][j - 1]:
                        dp[i][j].add(x ^ grid[i][j])
        return min(dp[-1][-1])
obj=Solution()
res=obj.minCost(grid=[[1,2,3],[3,4,5],[5,6,7]])
print(res)