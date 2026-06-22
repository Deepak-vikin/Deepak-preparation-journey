"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.



Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

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