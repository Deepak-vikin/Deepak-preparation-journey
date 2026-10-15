"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}

        def solve(s):
            if s > n:
                return float("inf")
            if s == n:
                return 0
            if s in dp:
                return dp[s]
            ans = float("inf")
            for i in range(1, isqrt(n) + 1):
                if s + i ** 2 <= n:
                    ans = min(ans, 1 + solve(s + i ** 2))
            dp[s] = ans
            return dp[s]
        return solve(0)
obj=Solution()
print(obj.numSquares(12))
print(obj.numSquares(3))
print(obj.numSquares(4))