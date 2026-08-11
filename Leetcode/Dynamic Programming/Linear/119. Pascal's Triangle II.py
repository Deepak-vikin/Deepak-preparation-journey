"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp=[]
        for i in range(1,rowIndex+2):
            dp.append([0]*i)
        dp[0][0]=1
        for i in range(1,rowIndex+1):
            for j in range(i+1):
                if j==0 or j==i:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
        return dp[-1]
obj=Solution()
res=obj.getRow(3)
print(res)
