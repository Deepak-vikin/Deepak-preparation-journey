"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[-1]*(n+1)
        if n==0 or n==1:
            return n
        dp[0]=0
        dp[1]=1
        def func(num):
            if num<0:
                return 0
            if dp[num]!=-1:
                return dp[num]
            dp[num]=func(num-1)+func(num-2)+func(num-3)
            return dp[num]
        return func(n)
obj=Solution()
res=obj.tribonacci(5)
print(res)