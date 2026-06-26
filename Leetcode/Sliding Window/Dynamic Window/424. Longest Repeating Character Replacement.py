"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        m=0
        f={}
        for r in range(len(s)):
            if s[r] in f:
                f[s[r]]+=1
            else:
                f[s[r]]=1
            d=(r-l+1)-max(f.values())
            while d>k:
                if f[s[l]]>1:
                    f[s[l]]-=1
                else:
                    del f[s[l]]
                l+=1
                d=(r-l+1)-max(f.values())
            m=max(m,r-l+1)
        return m
obj=Solution()
res=obj.characterReplacement("ABAB",2)
print(res)
