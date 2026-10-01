"""
Implement a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
"""
class Solution:
    def arraySign(self, nums: list[int]) -> int:
        if 0 in nums:
            return 0
        p=1
        for i in nums:
            p*=i
        def func(num):
            if num>0:
                return 1
            elif num<0:
                return -1
            else:
                return 0
        return func(p)
obj = Solution()
res = obj.arraySign([1,2,3,4,5])
print(res)