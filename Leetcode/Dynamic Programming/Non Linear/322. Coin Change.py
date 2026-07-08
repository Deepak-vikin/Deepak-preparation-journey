"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')] * (amount + 1) for _ in range(len(coins))]
        m = len(coins)
        n = amount + 1
        for i in range(m):
            dp[i][0] = 0
        for i in range(m):
            for j in range(1, n):
                if j >= coins[i]:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i]])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m - 1][n - 1] if dp[m - 1][n - 1] != float('inf') else -1

obj=Solution()
res=obj.coinChange([1,2,5], 10)
print(res)