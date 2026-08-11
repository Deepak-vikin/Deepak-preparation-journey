"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        dp=[]
        for i in range(1,n+1):
            dp.append([0]*i)
        dp[0][0]=1
        for i in range(1,len(dp)):
            for j in range(i+1):
                if j==0 or j==i:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
        return dp

obj=Solution()
print(obj.generate(5))

