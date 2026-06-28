"""
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous -k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!



Example 1:

Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
"""


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            for i in range(len(code)):
                code[i] = 0
            return code
        elif k > 0:
            d = code + code
            print(d)
            s = 0
            for i in range(1, k + 1):
                s += d[i]
            code[0] = s
            j = 1
            for i in range(k + 1, len(d)):
                s += d[i]
                s -= d[i - k]
                if j < len(code):
                    code[j] = s
                    j += 1
            return code
        elif k < 0:
            d = code + code
            k = abs(k)
            print(d)
            s = 0
            for i in range(len(code) - 1, len(code) - k - 1, -1):
                s += code[i]
            code[0] = s
            j = 1
            for i in range(len(code), len(d) - 1):
                s += d[i]
                s -= d[i - k]
                code[j] = s
                j += 1
            return code
obj=Solution()
res=obj.decrypt(code=[5,7,1,4], k=3)
print(res)
