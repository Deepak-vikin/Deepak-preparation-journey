"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.

Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the staircase, which is the position just past the last step (index cost.length).



Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost=cost+[0]
        dp=[-1]*(len(cost)+1)
        n=len(cost)
        def func(num,end):
            if num==end:
                return cost[end]
            if num<end:
                return 0
            if dp[num]!=-1:
                return dp[num]
            s1=cost[num]+func(num-1,end)
            s2=cost[num]+func(num-2,end)
            dp[num]=min(s1,s2)
            return dp[num]
        return min(func(n-1,0),func(n-1,1))
obj=Solution()
res=obj.minCostClimbingStairs([10,15,20])
print(res)