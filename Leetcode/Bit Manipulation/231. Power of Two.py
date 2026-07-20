"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return True if n & (n - 1) == 0 else False

obj=Solution()
print(obj.isPowerOfTwo(2))
print(obj.isPowerOfTwo(3))

"""
n & (n-1) removes the right most set bit.
12->1100
n-1 which is 11 -> 1011
n & (n-1) -> 1000
right most [1] set bit is removed.

For every power of Two it has only one [1] set bit so if we n & (n-1) for a Power of Two it becomes 0.
"""