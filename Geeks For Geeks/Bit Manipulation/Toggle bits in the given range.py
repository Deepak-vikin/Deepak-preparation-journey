"""
Given a non-negative number n and two values l and r. The problem is to toggle the bits in the range l to r in the binary representation of n, i.e., to toggle bits from the lth least significant bit to the rth least significant bit (the rightmost bit as counted as the first bit).

A toggle operation flips a bit 0 to 1 and a bit 1 to 0.

Example 1:

Input:
n = 17 , l = 2 , r = 3
Output:
23
Explanation:
(17)10 = (10001)2.  After toggling all
the bits from 2nd to 3rd position we get
(10111)2 = (23)10
"""

class Solution:
    def toggleBits(self, n , l , r):
        # code here
        mask=0
        l-=1
        r-=1
        for i in range(l,r+1):
            mask=mask|(1<<i)
        return mask^n
obj=Solution()
res =obj.toggleBits(17,2,3)
print(res)