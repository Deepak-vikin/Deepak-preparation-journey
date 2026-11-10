"""
You are climbing a staircase with n + 1 steps, numbered from 0 to n.

You are also given a 1-indexed integer array costs of length n, where costs[i] is the cost of step i.

From step i, you can jump only to step i + 1, i + 2, or i + 3. The cost of jumping from step i to step j is defined as: costs[j] + (j - i)2

You start from step 0 with cost = 0.

Return the minimum total cost to reach step n.



Example 1:

Input: n = 4, costs = [1,2,3,4]

Output: 13

Explanation:

One optimal path is 0 → 1 → 2 → 4

Jump	Cost Calculation	Cost
0 → 1	costs[1] + (1 - 0)2 = 1 + 1	2
1 → 2	costs[2] + (2 - 1)2 = 2 + 1	3
2 → 4	costs[4] + (4 - 2)2 = 4 + 4	8
Thus, the minimum total cost is 2 + 3 + 8 = 13
"""
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp=[-1]*(n+1)
        def solve(i):
            if i==n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            ans=float("inf")
            for j in range(1,4):
                if i+j<=n:
                    t=solve(i+j)+costs[i+j-1]+((j-i)+i)**2
                    ans=min(ans,t)
            dp[i]=ans
            return ans
        return solve(0)
obj=Solution()
res=obj.climbStairs(4,[1,2,3,4,5])
print(res)