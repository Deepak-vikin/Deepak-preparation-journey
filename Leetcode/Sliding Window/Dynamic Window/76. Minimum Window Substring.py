"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        f1={}
        for i in t:
            if i in f1:
                f1[i]+=1
            else:
                f1[i]=1
        left=0
        formed=0
        f={}
        ans=float('inf')
        start=0
        for right in range(len(s)):
            if s[right] in f:
                f[s[right]]+=1
            else:
                f[s[right]]=1
            if s[right] in f1 and s[right] in f and f[s[right]]==f1[s[right]]:
                formed+=1
            while formed==len(f1) and left<=right:
                if right-left+1<ans:
                    ans=right-left+1
                    start=left
                if s[left] in f:
                    f[s[left]]-=1
                if s[left] in f and s[left] in f1 and f[s[left]]<f1[s[left]]:
                    formed-=1
                if s[left] in f:
                    if f[s[left]]==0:
                        del f[s[left]]
                left+=1
        if ans==float("inf"):
            return ""
        return s[start:start+ans]
obj=Solution()
res=obj.minWindow("ADOBECODEBANC","ABC")
print(res)