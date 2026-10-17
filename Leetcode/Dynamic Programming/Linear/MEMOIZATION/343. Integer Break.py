"""
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.



Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        dp={}
        def solve(s,count):
            if (s,count) in dp:
                return dp[(s,count)]
            ans=0
            for i in range(1,n-s+1):
                if s+i==n:
                    if count>=1:
                        ans=max(ans,i)
                else:
                    ans=max(ans,i*solve(s+i,count+1))
            dp[(s,count)]=ans
            return ans
        return solve(0,0)
obj=Solution()
res=obj.integerBreak(10)
print(res)
