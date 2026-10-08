"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).



Example 1:


Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

from typing import List
"""

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows=len(matrix)
        dp=[[0]*rows for _ in range(rows)]
        for i in range(rows):
            for j in range(rows):
                if i==0:
                    dp[i][j]=matrix[i][j]
                else:
                    if j==0:
                        dp[i][j]=matrix[i][j]+min(dp[i-1][j],dp[i-1][j+1])
                    elif j==rows-1:
                        dp[i][j]=matrix[i][j]+min(dp[i-1][j],dp[i-1][j-1])
                    else:
                        dp[i][j]=matrix[i][j]+min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1])
        return min(dp[-1])
obj=Solution()
res=obj.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])
print(res)
