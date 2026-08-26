"""
An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

Given an integer n, return true if n is strictly palindromic and false otherwise.

A string is palindromic if it reads the same forward and backward.



Example 1:

Input: n = 9
Output: false
Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
In base 3: 9 = 100 (base 3), which is not palindromic.
Therefore, 9 is not strictly palindromic so we return false.
Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.
"""
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def calc(n,base):
            res=""
            while n>0:
                rem=n%base
                res=res+str(rem)
                n//=base
            return res
        for i in range(2,n-1):
            st=calc(n,i)
            if st==st[::-1]:
                continue
            return False
obj=Solution()
res=obj.isStrictlyPalindromic(9)
print(res)