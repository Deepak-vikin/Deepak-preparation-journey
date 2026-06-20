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


