"""
You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.

Note : If no such substring exists, return -1.

Examples:

Input: s = "aabacbebebe", k = 3
Output: 7
Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.

"""
class Solution:
    def longestKSubstr(self, s, k):
        f={}
        l=0
        m=0
        for r in range(len(s)):
            if s[r] in f:
                f[s[r]]+=1
            else:
                f[s[r]]=1
            while len(f)>k:
                if f[s[l]]>1:
                    f[s[l]]-=1
                else:
                    del f[s[l]]
                l+=1
            if len(f)==k:
                m=max(m,r-l+1)
        if len(f)<k:
            return -1
        return m
obj=Solution()
res=obj.longestKSubstr("aabacbebebe",3)
print(res)
