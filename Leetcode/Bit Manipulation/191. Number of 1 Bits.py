"""
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).



Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n!=0:
            n=n & (n-1)
            count+=1
        return count
obj=Solution()
print(obj.hammingWeight(11))