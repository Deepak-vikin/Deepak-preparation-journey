"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
"""


class Solution:
    def reverse(self, x: int) -> int:
        rv = 0
        n = abs(x)
        while n > 0:
            d = n % 10
            n = n // 10
            rv = rv * 10 + d
        if rv > 2 ** 31 - 1:
            return 0
        if x > 0:
            return rv
        else:
            return rv * -1
obj=Solution()
print(obj.reverse(123))
print(obj.reverse(-123))


