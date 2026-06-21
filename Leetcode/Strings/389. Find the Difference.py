class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a=0
        b=0
        for i in t:
            a+=ord(i)
        for i in s:
            b+=ord(i)
        return chr(abs(b-a))
obj=Solution()
res=obj.findTheDifference("abcd","abcde")
print(res)
