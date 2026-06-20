class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        c=0
        o=False
        for i in freq:
            c+=(freq[i]//2)*2
            if freq[i]%2!=0:
                o=True
        if o:
            c+=1
        return c
obj=Solution()
res=obj.longestPalindrome("babad")
print(res)