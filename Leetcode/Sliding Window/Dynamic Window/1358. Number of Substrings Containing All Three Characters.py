"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.



Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).

"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=0
        f={}
        l=0
        for r in range(len(s)):
            if s[r] in f:
                f[s[r]]+=1
            else:
                f[s[r]]=1
            while len(f)==3:
                count+=len(s)-r
                if f[s[l]]>1:
                    f[s[l]]-=1
                else:
                    del f[s[l]]
                l+=1
        return count

obj=Solution()
res=obj.numberOfSubstrings("abc")
print(res)

