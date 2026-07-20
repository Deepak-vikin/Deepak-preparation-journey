"""
Reverse bits of a given 32 bits signed integer.



Example 1:

Input: n = 43261596

Output: 964176192

Explanation:

Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        for _ in range(32):
            bit=n&1
            ans<<=1
            ans|=bit
            n=n>>1
        return ans
obj=Solution()
print(obj.reverseBits(43261596))