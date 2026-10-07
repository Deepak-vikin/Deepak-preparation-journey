"""
Given an integer array height[] where height[i] represents the height of the i-th stair, a frog starts from the first stair and wants to reach the last stair.

From any stair i, the frog has two options: it can either jump to the (i+1)th stair or the (i+2)th stair. The cost of a jump is the absolute difference in height between the two stairs.

Determine the minimum total cost required for the frog to reach the last stair.

Example:

Input: heights[] = [20, 30, 40, 20]
Output: 20
Explanation: Minimum cost is incurred when the frog jumps from stair 0 to 1 then 1 to 3:
jump from stair 0 to 1: cost = |30 - 20| = 10
jump from stair 1 to 3: cost = |20 - 30| = 10
Total Cost = 10 + 10 = 20
"""
class Solution:
    def minCost(self, height: list[int]) -> int:
        n=len(height)
        prev1=0
        prev2=0
        for i in range(1,len(height)):
            one=prev1+abs(height[i]-height[i-1])
            two=float("inf")
            if i>1:
                two=prev2+abs(height[i]-height[i-2])
            curr=min(one,two)
            prev2=prev1
            prev1=curr
        return prev1
obj = Solution()
res=obj.minCost([20, 30, 40, 20])
print(res)
