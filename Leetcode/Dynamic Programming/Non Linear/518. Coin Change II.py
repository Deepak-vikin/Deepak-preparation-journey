"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The final answer is guaranteed to fit into a signed 32-bit integer.



Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        rows=len(coins)
        cols=amount+1
        dp=[[0]*cols for _ in range(rows)]
        for i in range(rows):
            dp[i][0]=1
        for i in range(rows):
            for j in range(cols):
                if j>=coins[i]:
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[rows-1][cols-1]
obj=Solution()
res=obj.change(5, [1,2,5])
print(res)