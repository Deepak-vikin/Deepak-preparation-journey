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
        if n==0:
            return 0
        if n<=2:
            return 1
        prev1=0
        prev2=1
        prev3=1
        for i in range(3,n+1):
            curr=prev1+prev2+prev3
            prev1=prev2
            prev2=prev3
            prev3=curr
        return prev3
obj=Solution()
res=obj.tribonacci(5)
print(res);