"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:

Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
"""
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        dp = [[None] * n for _ in range(n)]

        def func(row, prev):
            if row == 0:
                min_elem = float("inf")
                for i in range(n):
                    if i in (prev, prev + 1, prev - 1) and i >= 0 and i < n:
                        min_elem = min(min_elem, matrix[0][i])
                return min_elem
            if dp[row][prev] is not None:
                return dp[row][prev]
            min_sum = float("inf")
            for i in range(n):
                if i in (prev, prev - 1, prev + 1) and i >= 0 and i < n:
                    s = matrix[row][i] + func(row - 1, i)
                    min_sum = min(min_sum, s)
            dp[row][prev] = min_sum
            return dp[row][prev]

        ans = float("inf")
        for i in range(n):
            s = matrix[n - 1][i] + func(n - 2, i)
            ans = min(ans, s)
        return ans
obj=Solution()
res=obj.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])
print(res)

