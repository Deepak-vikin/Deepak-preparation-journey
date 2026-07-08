"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.



Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows=len(triangle)
        cols=len(triangle)
        dp=[]
        for i in range(rows):
            row=[]
            for j in range(i+1):
                row.append(0)
            dp.append(row)
        for i in range(rows):
            for j in range(i+1):
                if i==0 and j==0:
                    dp[i][j]=triangle[i][j]
                elif j==0:
                    dp[i][j]=triangle[i][j]+dp[i-1][j]
                elif j==i:
                    dp[i][j]=triangle[i][j]+dp[i-1][j-1]
                else:
                    dp[i][j]=triangle[i][j]+min(dp[i-1][j-1],dp[i-1][j])
        return min(dp[-1])
obj=Solution()
res=obj.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(res)